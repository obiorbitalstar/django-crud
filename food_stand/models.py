from django.db import models
from django.urls import reverse
# Create your models here.

class Menu(models.Model):
    dish_name = models.CharField(max_length = 64) 
    customer =models.ForeignKey('auth.user',on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.dish_name
    def get_absolute_url(self):
        return reverse('home')
        

