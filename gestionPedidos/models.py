from django.db import models

# Create your models here.
#se crea una clase por cada tabla que necesites que tenga tu BBDD

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    #verbose_name="Dirección de envío" - con verbose_name cambiamos como queremos que se vea ese campo en el admin sin cambiarlo en la tabla
    direccion = models.CharField(max_length=50, verbose_name="Dirección de envío")
    #(blank=True, null=True) es para hacer que el campo no sea obligatorio si no OPCIONAL
    email = models.EmailField(blank=True, null=True)
    tfno = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    