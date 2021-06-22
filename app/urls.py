from django.contrib import admin
from django.urls import path

from core.views import post, profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<slug:slug>', post, name='post'),
    path('profile/<username>', profile, name='profile'),
]
