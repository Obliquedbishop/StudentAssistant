from django.db import models

# Create your models here.
class career(models.Model):
    firstname = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
