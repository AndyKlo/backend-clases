from django.db import models

# Create your models here.
#Code First(hago el codigo y ahi se crea la bdd)
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre + " " + self.apellido

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    eliminado = models.BooleanField(default=False)
    def __str__ (self):
       return self.nombre #+ " " + str(self.precio)
    
class Venta(models.Model):
    fecha = models.DateTimeField("fecha venta")
    monto = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta,on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()