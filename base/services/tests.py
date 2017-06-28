from django.test import TestCase
from services.models import User, Client
from services.serializers import UserSerializer
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core import serializers
from services.gitdam import GDAM
from services.gitdam import STREAMS
from git import Repo
from services.termsign import TermSign


#
# {'repositoryMetadata': {'accountId': '089144853166', 'repositoryId': '0d017793-2145-4fe8-a893-2417c8d66b2e', 
#'repositoryName': '455e85ea-98e4-438a-b11e-60adec661c05', 'repositoryDescription': 'Client1', 
#'lastModifiedDate': datetime.datetime(2017, 4, 25, 5, 26, 51, 278000, tzinfo=tzlocal()), 
#'creationDate': datetime.datetime(2017, 4, 25, 5, 26, 51, 278000, tzinfo=tzlocal()), 
#'cloneUrlHttp': 'https://git-codecommit.us-east-1.amazonaws.com/v1/repos/455e85ea-98e4-438a-b11e-60adec661c05', 
#'cloneUrlSsh': 'ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/455e85ea-98e4-438a-b11e-60adec661c05', 
#'Arn': 'arn:aws:codecommit:us-east-1:089144853166:455e85ea-98e4-438a-b11e-60adec661c05'}, 
#'ResponseMetadata': {'RequestId': 'c916ef92-2977-11e7-b825-6f1a6e3f2382', 'HTTPStatusCode': 200, 
#                     'HTTPHeaders': {'x-amzn-requestid': 'c916ef92-2977-11e7-b825-6f1a6e3f2382', 'content-type': 'application/x-amz-json-1.1', 'content-length': '567', 'date': 'Tue, 25 Apr 2017 05:26:50 GMT'}, 'RetryAttempts': 0}}
#
class UserTestCase(TestCase):
    def setUp(self) :
        #u = User.objects.create(id="3423423423423", handle="AAAAAAA")
        #u.save()
        
        #serializer = UserSerializer(u)
        #print(serializer.data)
        print(' ')

       
    def test_GDAM1(self):
         #g = GDAM("AAAAAAA", "/Users/mikem/development/work/testa", "juddy", 'testa', 'ssh://git-codecommit.us-west-2.amazonaws.com/v1/repos/testa', STREAMS.work)
         #g.createDocument("qedijowoiefjowiefhowhefowhefddqed 112222", "third2.txt")
         #g.updateDocument("ABC123", "third2.txt", STREAMS.work)
         #ans = g.getDocument("third2.txt", STREAMS.work)
         #g.moveDocument("third2.txt", STREAMS.work, STREAMS.test)
         #f = g.getDocumentByVer("third.txt", "26dcd930577c77980d2d082ab537e66e02700678")
         print('')
    
    def test_ClientReg(self) :
        t = TermSign("7813628736487236487236482", '/var/tmp/termsign')
        client = Client(name='Client1')
        cli = t.registerClient(client)
        user = User(clientId=cli.id, name='test1', password='111')
        t.registerUser(cli, user)

