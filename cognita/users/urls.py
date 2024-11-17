from django.urls import path
from .views import *


urlpatterns = [
    path('home/', index, name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user)
]