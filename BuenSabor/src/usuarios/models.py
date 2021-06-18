from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    imagen = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=254)
    telefono = models.CharField("Teléfono",max_length=15)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Domicilio(models.Model):
    calle=
