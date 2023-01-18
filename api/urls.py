from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('app.urls')),
    # path('products/', include('app.urls')),
    path('products/create/', include('app.urls')),
]
