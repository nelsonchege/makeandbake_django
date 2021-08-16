from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class StreamingPlatform(models.Model):
    name    = models.CharField(max_length=30)
    about   = models.CharField(max_length=200)
    website = models.URLField(max_length=200) 

    def __str__(self):
        return self.name

class Watchlist(models.Model):
     title       = models.CharField(max_length=50)
     type        = models.CharField(max_length=50)
     platform    = models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE,related_name="watchlist")
     description = models.CharField(max_length=500)  
     active      = models.BooleanField(default=True)
     created     = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.title

class Review(models.Model):
    ratings     = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    watchlist   = models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="reviews")
    author      = models.ForeignKey( User,on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.watchlist.title+" : "+str(self.ratings)