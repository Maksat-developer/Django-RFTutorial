from .views import user_model_detail, user_model_list_create
from django.urls import path 


urlpatterns = [
    path('user-list/', user_model_list_create),
    path('user-detail/<int:pk>/', user_model_detail),

]