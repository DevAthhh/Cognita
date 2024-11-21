from django.urls import path
from .views import *

urlpatterns: list = [
    path('', Index.as_view(), name='dashboard'),                # -> Main page without note
    path('note/<int:note_id>/', Note.as_view(), name='note'),   # -> Main page with open note
    path('create/', create, name='create'),                     # -> Create url
    path('note/<int:note_id>/update/', update, name='update'),  # -> Update url
]