from django.db import models

# Create your models here.

class Servicio(models.Model):
    id            = models.CharField(primary_key=True, max_length=10)
    precio          = models.CharField(max_length=10)
    foto            = models.ImageField(upload_to='media/')
    descripcion     = models.CharField(max_length=50)