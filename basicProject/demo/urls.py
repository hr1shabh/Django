
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_demo, name='all_demo'),
    path('<int:car_id>/', views.car_details, name='car_details'),
    path('car_stores/', views.car_stores, name = 'car_stores'),
]
