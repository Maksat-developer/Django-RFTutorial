from django.shortcuts import render

from rest_framework import generics, permissions



from .models import UserModel, UserProfile
from .serializers import UserModelSerializer, UserProfileSerializer
from rest_framework import permissions


class UserModelListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAdminUser]

user_model_list_create = UserModelListCreateView.as_view()


class UserModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAdminUser]

user_model_detail = UserModelDetailView.as_view()



class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.BasePermission]

user_profile_list_create = UserProfileListCreateView.as_view()


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.BasePermission]
user_profile_detail = UserProfileDetailView.as_view()



