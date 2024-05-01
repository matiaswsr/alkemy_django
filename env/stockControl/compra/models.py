from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    apellido = models.CharField("Apellido", max_length=100)
    dni = models.IntegerField("DNI")

    def __str__(self):
        return self.nombre + " " + self.apellido

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.IntegerField("Precio")
    stock_actual = models.IntegerField("Stock")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre