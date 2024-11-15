# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage
    path('products/', views.product_list, name='product_list'),  # Product list
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Product detail
]
