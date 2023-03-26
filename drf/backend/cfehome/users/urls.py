from .views import *
from django.urls import path 


urlpatterns = [

    path('user-model-list/', user_model_list_create),
    path('user-model-detail/<int:pk>/', user_model_detail),


    path('user-profile-list/', user_profile_list_create),
    path('user-profile-detail/<int:pk>/', user_profile_detail),

]