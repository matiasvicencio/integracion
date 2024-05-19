from django.db import models

# Create your models here.

class producto(models.Model):
    cod_producto = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.precio)
