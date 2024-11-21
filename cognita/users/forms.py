from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    """
    the form for
    the login of site users...
    """

    class Meta:
        model = get_user_model()
        fields: tuple = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    """
    user registration form...
    """

    class Meta:
        model = get_user_model()
        fields: tuple = ('username', 'email', 'password1', 'password2')
