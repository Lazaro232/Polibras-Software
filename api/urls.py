from app.api import viewsets
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

route = routers.DefaultRouter()
route.register(r'products', viewsets.ProductViewSet)
route.register(r'payments', viewsets.PaymentViewSet)
route.register(r'sales', viewsets.SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(route.urls)),
]
