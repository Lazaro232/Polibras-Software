from app import models
from app.api import serializers
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.query import QuerySet


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Payments.objects.all()
    serializer_class = serializers.PaymentSerializer


class SaleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Sales.objects.all()
    serializer_class = serializers.SaleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # No date passed
        if not queryset:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                # Ensure queryset is re-evaluated on each request.
                queryset = queryset.all()
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)

        return Response(queryset)

    def get_queryset(self):
        date = self.request.query_params.get('date', None)
        if date:
            # Group and order by date to sum
            queryset = models.Sales.objects.values(
                'date').order_by('date').annotate(
                    total_amount_sold=Sum('amount_sold')).filter(date=date)
            # No sales detected
            if not queryset:
                queryset = [{"date": date, "total_amount_sold": 0.0}]

            return queryset

        return []

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
