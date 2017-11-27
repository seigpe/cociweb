from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)


class Contratos(models.Model):
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

