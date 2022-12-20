from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.google_auth, name='google_auth'),
]