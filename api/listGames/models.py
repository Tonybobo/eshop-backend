from locale import currency
from turtle import title
from django.db import models

# Create your models here.
class Games(models.Model):
    gamesId = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()
    currency = models.CharField(max_length=10)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.CharField(max_length=100)
    lowestPrice = models.DecimalField(max_digits=10, decimal_places=2)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.TextField()
    releaseDate = models.DateField()
    
class Currency(models.Model):
    currencyId = models.CharField(max_length=100)
    rates = models.FloatField()