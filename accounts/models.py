from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length = 100)
    Email = models.EmailField(max_length = 100)
