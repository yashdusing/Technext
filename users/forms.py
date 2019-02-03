from django import forms
from django.contrib.auth.forms import User,UserCreationForm
from .models import Profile
import datetime


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [ 'username', 'password1', 'password2']



'''
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = [ 'username','email','company', 'password1', 'password2']
'''
