from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='portal' )
]
