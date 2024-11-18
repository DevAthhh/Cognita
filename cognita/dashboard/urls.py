from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dashboard'),
    path('note/<int:note_id>/', note, name='note'),
    path('create/', create, name='create')
]