from django.db import models
from django.template.defaultfilters import default
from datetime import datetime, timedelta

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    clientId = models.CharField(max_length=64, default='')    
    name = models.CharField(max_length=128, default='')
    handle = models.CharField(max_length=64, default='')
    password = models.CharField(max_length=64, default='')
    tms = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    name = models.CharField(max_length=128)
    apikey = models.CharField(max_length=512, default='')
    sshurl = models.CharField(max_length=1024, default='')
    tms = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    id = models.CharField(max_length=64,primary_key=True)    
    clientId = models.CharField(max_length=64)    
    name = models.CharField(max_length=128)
    tms = models.DateTimeField(auto_now_add=True)

class Signature(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    clientId = models.CharField(max_length=64)    
    documentId = models.CharField(max_length=64)    
    version = models.CharField(max_length=128)
    tms = models.DateTimeField(auto_now_add=True)

class SignatureDetail(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    signatureId = models.CharField(max_length=64)    
    part =  models.CharField(max_length=256)   
    state = models.IntegerField
    tms = models.DateTimeField(auto_now_add=True)

