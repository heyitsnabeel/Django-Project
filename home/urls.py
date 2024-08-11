from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('/index',views.index),
    path('/service',views.service),
    path('/contact',views.contact),
]