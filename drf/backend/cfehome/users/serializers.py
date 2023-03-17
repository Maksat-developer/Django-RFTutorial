from rest_framework import serializers
from .models import UserModel, UserProfile

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class UserProfileSerialier(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

        