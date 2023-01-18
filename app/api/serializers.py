from app import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payments
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sales
        fields = '__all__'
        # fields = ['product', 'payment', 'quantity_sold']
