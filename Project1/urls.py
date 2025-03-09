
from django.urls import path
from app1.views import *

urlpatterns = [
    path('', home, name='home'),
    path('index2', index2, name='index2'),
]
