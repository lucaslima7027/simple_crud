from django.db import models

class Product(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Stock(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

# Create your models here.
