from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('test', views.test, name='test'),
    path('check_login_password', views.check_login_password, name='check_login_password'),
]