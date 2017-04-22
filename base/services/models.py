from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    clientId = models.CharField(max_length=64)    
    name = models.CharField(max_length=128)
    handle = models.CharField(max_length=64)
    tms = models.TimeField()

class Client(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    name = models.CharField(max_length=128)
    tms = models.TimeField()

class Document(models.Model):
    id = models.CharField(max_length=64,primary_key=True)    
    clientId = models.CharField(max_length=64)    
    name = models.CharField(max_length=128)
    tms = models.TimeField()

class Signature(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    clientId = models.CharField(max_length=64)    
    documentId = models.CharField(max_length=64)    
    version = models.CharField(max_length=128)
    tms = models.TimeField()

class SignatureDetail(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    signatureId = models.CharField(max_length=64)    
    part =  models.CharField(max_length=256)   
    state = models.IntegerField
    tms = models.TimeField()

