from django import forms
from django.contrib.auth.models import User # built-in user model
from django.contrib.auth.forms import UserCreationForm # built-in form for creating new users

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # email field

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] # fields to show in form (in order)

    