from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Book(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    data_create = models.DateTimeField(auto_now_add=True)
    data_time_mod = models.DateField(auto_now=True)
    user_age = models.IntegerField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
    
    
    
    def __str__(self):
        return f'{self.name}'