from django.urls import path

from .views import *

urlpatterns = [
    path('logout', Logout.as_view(), name='logout'),
]