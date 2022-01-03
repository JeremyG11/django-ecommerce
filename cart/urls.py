
from django.urls import path 

from . import views

app_name = 'Cart'

urlpatterns = [
    path('', views.cart_summary, name = 'cart'),
    path('add', views.cart_add, name = 'cart_add'),
]