from app import models
from app.api import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payments.objects.all()
    serializer_class = serializers.PaymentSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sales.objects.all()
    serializer_class = serializers.SaleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.SaleSerializer(data=data)
        if serializer.is_valid():
            # Sale informations
            quantity_sold = serializer.validated_data.get('quantity_sold')
            product_id = serializer.validated_data.get('product').id
            # Product stock informations
            product = models.Products.objects.get(id=product_id)
            stock_before_sale = int(product.stock)
            stock_after_sale = stock_before_sale - int(quantity_sold)
            # Product price informations
            price = product.price
            amount_sold = price * quantity_sold
            # Stock validation
            if stock_after_sale < 0:
                return Response({"message": "Insufficient stock"},
                                status.HTTP_400_BAD_REQUEST)
            else:
                # Updating product stock
                product.stock = stock_after_sale
                # Creating a copy to add the amount_sold field
                serialized_data = serializer.data
                serialized_data['amount_sold'] = amount_sold
                updated_serializer = serializers.SaleSerializer(
                    data=serialized_data)
                # Saving product and sale informations
                if updated_serializer.is_valid():
                    product.save()
                    updated_serializer.save()

            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
