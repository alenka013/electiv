from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('login/', loginpage),
    path('electivepage/<slug:elid>/', electivepage),
]