from django.urls import path
from immobiles.views import *

app_name = 'immobiles'

urlpatterns = [
    path('create-customer/', create_customer, name="create-customer"),
    path('list-customer/', list_customer, name="list-customer"),
    path('update-customer/<int:pk>/', update_customer, name="update-customer"),
    path('delete-customer/<int:pk>/', delete_customer, name="delete-customer"),

    path('create-immobile/', create_immobile, name='create-immobile'),  
    path('', list_immobile, name="list-immobile"),
    path('update-immobile/<int:pk>/', update_immobile, name="update-immobile"),
    path('delete-immobile/<int:pk>/', delete_immobile, name="delete-immobile"),
    path('delete-image/<int:pk>/', delete_image, name="delete-image"),
    
    path('create-register/<int:id>/', create_register, name='create-register'), 
    path('list-report/', list_report, name='list-report'), 
]
