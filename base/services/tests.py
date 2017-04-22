from django.test import TestCase
from services.models import User
from services.serializers import UserSerializer
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core import serializers
from services.gitdam import GDAM
from services.gitdam import STREAMS
from git import Repo



class UserTestCase(TestCase):
    def setUp(self) :
        u = User.objects.create(id="3423423423423", handle="AAAAAAA")
        u.save()
        
        serializer = UserSerializer(u)
        print(serializer.data)

    def test_animals_can_speak(self):
        u = User.objects.get(id="3423423423423")
       
    def test_GDAM1(self):
         g = GDAM("AAAAAAA", "/Users/mikem/development/work/testa", "juddy", 'testa', 'ssh://git-codecommit.us-west-2.amazonaws.com/v1/repos/testa', STREAMS.work)
         #g.createDocument("qedijowoiefjowiefhowhefowhefddqed 112222", "third2.txt")
         #g.updateDocument("ABC123", "third2.txt", STREAMS.work)
         #ans = g.getDocument("third2.txt", STREAMS.work)
         #g.moveDocument("third2.txt", STREAMS.work, STREAMS.test)
         f = g.getDocumentByVer("third.txt", "26dcd930577c77980d2d082ab537e66e02700678")
         print(f)
         
        
        