from django.db import models

# Create your models here.
class allprice(models.Model):
    id = models.AutoField(primary_key=True)
    stockid = models.CharField(max_length = 10)
    date = models.CharField(max_length = 10)
    price = models.DecimalField(max_digits = 11,decimal_places=0,default=0)

class allstock(models.Model):
    stockid = models.CharField(max_length=10,primary_key=True)
    stockname = models.CharField(max_length = 15)
