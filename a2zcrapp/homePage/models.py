from django.db import models

class allProducts(models.Model):
    product_name=models.CharField(max_length=200)
    product_price=models.IntegerField()
    product_rating=models.FloatField()
    