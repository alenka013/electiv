from django.contrib import admin
from django.urls import path, include
from myapp1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls'))
]
