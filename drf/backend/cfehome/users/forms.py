from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = UserModel
        fields = ('email',)



class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserModel
        fields = ('email',)
        