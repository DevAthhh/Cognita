from django import forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


# ----- TESTING BLOCK -----
def index(request):
    return HttpResponse(f'Hello {request.user}')
# ----- END TESTING BLOCK -----

class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/auth.html'
    extra_context = {'title': 'login'}

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/auth.html'
    extra_context = {'title': 'register'}

    def get_success_url(self):
        return reverse_lazy('login')

# ----- view's function -----

def logout_user(request):
    logout(request)
    return redirect('home')