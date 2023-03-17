from django.shortcuts import render

from rest_framework import generics, permissions



from .models import UserModel, UserProfile
from .serializers import UserModelSerializer, UserProfileSerialier


class UserModelListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

user_model_list_create = UserModelListCreateView.as_view()


class UserModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

user_model_detail = UserModelDetailView




