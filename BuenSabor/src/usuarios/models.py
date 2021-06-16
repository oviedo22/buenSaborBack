from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField("First name", max_length=255)
    apellido = models.CharField("Last name", max_length=255)
    dni = models.CharField("Dni",max_length=10)
    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    imagen = models.ImageField(upload_to='myphoto/%Y/%m/%d/', null=True, max_length=254)
    telefono = models.CharField("Teléfono",max_length=15)

    def __str__(self):
        return self.nombre + " " + self.apellido
