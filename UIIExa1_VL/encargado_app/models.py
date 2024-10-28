from django.db import models

# Create your models here.

class Encargado(models.Model):
    id_encargado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    curp=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre