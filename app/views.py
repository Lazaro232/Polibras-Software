from app import models
from app.api import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = models.Products.objects.all()
        serializer = serializers.ProductsSerializer(products, many=True)

        return Response(serializer.data)

    serializer = serializers.ProductsSerializer(data=request.data)
    # Valid product
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Invalid product
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
