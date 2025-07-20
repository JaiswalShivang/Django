from django.contrib import admin
from django.urls import path,include
from api.views import *
  
urlpatterns = [
    path('',index,name="indexpage"),
]