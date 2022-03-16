from django.db import models

# Create your models here.
class Familia(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()