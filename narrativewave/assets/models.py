from django.db import models
from django.db.models.base import Model

# Create your models here.

class Asset(models.Model):
  name = models.CharField(max_length=5)


class Column(models.Model):
  asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  value = models.CharField(max_length=50)
  timestamp = models.DateTimeField()
