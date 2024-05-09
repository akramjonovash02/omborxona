from django.urls import path

from .views import *

urlpatterns = [
    path('mahsulotlar/', Mahsulotlar.as_view(), name='mahsulotlar'),
    path('mijozlar/', Mijozlar.as_view(), name='mijozlar'),
    path('delete/<int:mahsulot_id>/', MahsulotDeleteView.as_view, name='delete_product')
]