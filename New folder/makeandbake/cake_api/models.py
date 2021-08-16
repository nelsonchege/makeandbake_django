from django.db import models

# Create your models here.
class CakeVariety(models.Model):
    variety = models.CharField(max_length=100)
    

    def __str__(self):
        return self.variety

class DisplayCakes(models.Model):
    cake_name   = models.CharField(max_length=200)
    cake_type   = models.ForeignKey(CakeVariety,on_delete=models.CASCADE,related_name="displaycakes")
    description = models.CharField(max_length=500)
    price       = models.IntegerField()
    weight      = models.FloatField()
    offer       = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cake_name

class CakeOrder(models.Model):
    name           = models.CharField(max_length=200)
    phone_number   = models.CharField(max_length=200)
    email          = models.CharField(max_length=200)
    delivered_by   = models.CharField(max_length=200)
    cake_selected  = models.ForeignKey(DisplayCakes,on_delete=models.CASCADE,related_name="cakeorder")
    quantity       = models.IntegerField()
    
    def __str__(self):
        return self.name

class Testdb(models.Model):
    name    = models.CharField(max_length=200)

    def __str__(self):
        return self.name
