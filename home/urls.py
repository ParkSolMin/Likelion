from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('', home.views.intro, name='intro'),
]