from django.urls import path

from .views import *

urlpatterns = [
    path('statistiklar/', Stats.as_view(), name='stats')
]