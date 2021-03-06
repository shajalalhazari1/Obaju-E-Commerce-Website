from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('shipping-address/', views.shipping_address, name="shipping_address"),
    path('delivery-method/', views.delivery_method, name="delivery_method"),
    path('', views.payment, name="payment"),
    path('order-review/', views.order_review, name="order_review"),
    path('success/', views.success, name="success"),
]