from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(default='')
