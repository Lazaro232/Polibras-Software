from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.api import viewsets

route = routers.DefaultRouter()
route.register(r'products', viewsets.ProductViewSet)
route.register(r'payments', viewsets.PaymentViewSet)
route.register(r'sales', viewsets.SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
