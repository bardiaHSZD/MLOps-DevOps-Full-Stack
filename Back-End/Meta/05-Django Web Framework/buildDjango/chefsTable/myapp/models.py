from django.db import models

# Create your models here.
from unicodedata import name

class Menu(models.Model):
    name = models.CharField(max_length= 100)
    cuisine = models.CharField(max_length= 100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name + ":" +  self.cuisine