from django.db import models

# Create your models here.
class Blogs(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    author      = models.CharField(max_length=200)