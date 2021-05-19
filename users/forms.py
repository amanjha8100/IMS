from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(forms.PasswordInput())
    # password2 = forms.CharField