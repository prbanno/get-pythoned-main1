from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=50,required=True)
    email=forms.EmailField(max_length=50,required=True)
    password= forms.CharField(max_length=50, required=True)

    class Meta:
        model=User
        fields=['username','email','password']
