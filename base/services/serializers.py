from rest_framework import serializers
from services.models import User
from services.models import Client
from services.models import Document
from services.models import Signature


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'handle', 'clientId', 'tms', 'name')    

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name', 'clientId', 'tms')    

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ('id', 'documentId', 'clientId', 'version', 'tms')    

