from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:slug>/', views.product_detail, name ="product_detail")
]