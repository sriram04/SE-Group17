from django import forms
# from .models import REG_USER
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from twitter.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "name":"username",
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password  = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "name":"password",
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
