from django import forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name: str = 'users/auth.html'
    extra_context: dict = {'title': 'login'}

    def get_success_url(self):
        return reverse_lazy('dashboard')


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name: str = 'users/auth.html'
    extra_context: dict = {'title': 'register'}

    def get_success_url(self):
        return reverse_lazy('login')


# ----- view's function -----

def logout_user(request):
    """
    This foo for logout user

    :param request:
    :return:
    """

    logout(request)
    return redirect('dashboard')