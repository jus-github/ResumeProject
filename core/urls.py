
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from core import views

urlpatterns = [
    path('', views.home , name='home'),
     path('contact', views.contact , name='contact'),
   
]
