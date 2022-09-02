from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
# from django.forms import widgets
from django import forms
class Form(UserCreationForm):
    # password2=forms.CharField(label="confirm pass",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        # labels={'email':'Email'}

class profileform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
