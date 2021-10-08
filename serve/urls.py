
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from serve import views

urlpatterns = [
    path('services/', views.services , name='services'),
   
]
