# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home-view'),
    path('delete/<pk>/', LinkDeleteView.as_view(), name='delete-view'),
    path('update/', UpdatePrices, name='update-prices'),
]
