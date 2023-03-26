from rest_framework import serializers
from .models import UserModel, UserProfile

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("email", 'password',)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "phone"



        