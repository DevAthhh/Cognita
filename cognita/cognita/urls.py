from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

from .exceptions import except404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include('users.urls')),
    path('', include('dashboard.urls'))
]

handler404 = except404
