from rest_framework import serializers
from services.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'handle', 'clientId', 'tms', 'name')    
