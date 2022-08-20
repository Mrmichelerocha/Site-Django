from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Customer(models.Model):
  username = models.CharField(max_length=150, null=True)
  email = models.EmailField(max_length=100)
  password1 = models.CharField(max_length=15)
  password2 = models.CharField(max_length=15)
  
  def __str__(self):
    return self.username