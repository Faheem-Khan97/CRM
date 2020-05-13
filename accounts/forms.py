from django.forms import ModelForm
from .models import *

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class customerForm(ModelForm):
    class Meta:
        model = customer
        fields =  '__all__'
        exclude = ['user']

class orderForm(ModelForm):
    class Meta:
        model = order
        fields =  '__all__'

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']