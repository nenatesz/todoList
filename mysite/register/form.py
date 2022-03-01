from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    # define that this form will save in the user database
    class Meta:
        # this defines that we are going to change the user model whenever we change something in this form
        model = User
        # the fileds property lays out how we want the form to be
        fields = ["username", "email", "password1", "password2"]