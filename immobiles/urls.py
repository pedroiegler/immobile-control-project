from django.urls import path
from immobiles.views import *

app_name = 'immobiles'

urlpatterns = [
    path('create-customer/', create_customer, name="create-customer"),
    path('list-customer/', list_customer, name="list-customer"),
    path('update-customer/<int:pk>/', update_customer, name="update-customer"),

    path('create-immobile/', create_immobile, name='create-immobile'),  
    path('list-immobile/', list_immobile, name="list-immobile"),
    path('update-immobile/<int:pk>/', update_immobile, name="update-immobile"),
    
    path('create-register/<int:id>/', create_register, name='create-register'), 
    path('list-report/', list_report, name='list-report'), 
]
