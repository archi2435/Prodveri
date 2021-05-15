from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    
    path('basket_adding', views.basket_adding, name='basket_adding'),
    
]