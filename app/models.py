from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150)
    stock = models.IntegerField(default=0)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Payments(models.Model):
    method = models.CharField(max_length=200)


class Sales(models.Model):
    product = models.ForeignKey(
        Products, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(
        Payments, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_sold = models.IntegerField(null=True, blank=True)
    amount_sold = models.FloatField(default=0.0)
    date = models.DateField(auto_now_add=True)
