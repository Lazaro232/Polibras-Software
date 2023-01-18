from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
