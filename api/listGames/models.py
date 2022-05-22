from django.db import models

# Create your models here.
class Games(models.Model):
    id = models.CharField(max_length=100 , primary_key=True)
    title = models.TextField()
    description = models.TextField()
    currency = models.CharField(max_length=10)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.CharField(max_length=100)
    lowestPrice = models.DecimalField(max_digits=10, decimal_places=2)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    publishers = models.TextField()
    releaseDate = models.DateField()
    
    class Meta:
        ordering = ['title']
        db_table = "games"
    
class Currency(models.Model):
    id = models.CharField(max_length=100 , primary_key=True)
    rate = models.DecimalField(max_digits=10 , decimal_places= 5)
    
    class Meta:
        ordering = ['id']
        db_table = "currency"