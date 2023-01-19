from app.api import viewsets
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Routes
route = routers.DefaultRouter()
route.register(r'products', viewsets.ProductViewSet)
route.register(r'payments', viewsets.PaymentViewSet)
route.register(r'sales', viewsets.SaleViewSet)
# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Sales API",
        default_version="1.0.0",
        description="API documentation of App"
    ),
    public=True
)
# Urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('swagger/schema/', schema_view.with_ui('swagger',
         cache_timeout=0), name="swagger-schema"),
    path('', include(route.urls)),
]
