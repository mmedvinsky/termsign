from enum import Enum
import os
import string
import base64
import uuid
from services.models import User
from services.models import Client
import logging
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from datetime import datetime, timedelta
import boto3

''' 
  TermSign API.  All functions for termsign will be there
'''  
class TermSign(object):
    def __init__(self, encKey):
        self.encKey = encKey
        self.awsCodeCommit = boto3.client('codecommit')
        
    def check_password(self, clear_password, password_hash):
        return SHA256.new(clear_password).hexdigest() == password_hash
#    
    #
    # Build session string
    def build_session_string(self, user, client) :
        return '{0}|{1}|{2}'.format(client.id, user.id, datetime.now)
     
    def encrypt_session(self, sess) :
         aes = AES.new(self.encKey, AES.MODE_CBC)
         return base64.b64encode(aes.encrypt(sess))

    def descrypt_session(self, sess) :
         aes = AES.new(self.encKey, AES.MODE_CBC)
         return aes.decrypt(base64.b64decode(sess))

#
# Register new Client.
#
    def registerClient(self, client) :
        client.id = uuid.uuid4()
        client.apikey = uuid.uuid4()
        cli = Client.objects.create(id=str(uuid.uuid4()), apikey=str(uuid.uuid4()), name=client.name)
        response = self.awsCodeCommit.create_repository(repositoryName=str(cli.id), repositoryDescription=cli.name)
        cli.sshurl = response.cloneUrlSsh
        cli.save()
        return cli
#
# Register new User.
#
    def registerUser(self, client, user) :
        cli = self.getClientById()
        if not cli :
           logging.error('E_NoClient')
           raise ValueError('E_NoClient')
        return User.objects.create(id=uuid.uuid4(), clientId=cli.id, name=user.name, password=user.password)
#
# Lookup new Client.
#
    def getClientById(self, clientId) :
        return Client.objects.get(id=uuid.uuid4())
        
    def getClientByApiKey(self, akey) :
        return Client.objects.get(apikey=akey)
        
    def getClientWithCheck(self, clientId, a) :
        return Client.objects.get(id=uuid.uuid4(), apikey=a)
        
# Login into TermSign enviornment 
# and get session
#
    def open(self, client, user) :
        c = Client.objects.get(apikey=client.apikey)
        if  not c :
            logging.error('E_NoClient')
            raise ValueError('E_NoClient')
            
        u = User.objects.get(name=user.name, clientId=client.id)
        if  not u :
            logging.error('E_NoUserForClient %s', user.id)
            raise ValueError('E_NoUserForClient  %s', user.id)
        #
        # Get the hashed value and hash the provided password to check.
        #
        if not self.check_password(user.password, u.password) :
            logging.error('E_LoginFailed %s %s', c.id, u.id)
            raise ValueError('E_LoginFailed %s %s', c.id, u.id)
        return self.encrypt_session(self.build_session_string(u, c)) 
        