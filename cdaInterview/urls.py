from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
     path('',views.loginView , name='login'),
     path('main/',views.main, name='main'),
     path('contact-us/',views.contactUs, name='contact-us')
]