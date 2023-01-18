from app import views
from django.urls import path

urlpatterns = [
    path('', views.get_products_list),
    path('', views.create_product)
]
