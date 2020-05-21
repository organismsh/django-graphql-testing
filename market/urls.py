from django.urls import path
from .import views

urlpatterns = [
    path('add_category', views.add_category, name='add_category'),
    path('add_product', views.add_product, name='add_product'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart')
]
