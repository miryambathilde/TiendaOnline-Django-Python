from django.contrib import admin
#importacion de tabla clientes desde el archivo gestionPedidos-models.py
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

#linea de codigo para tener desde el admin disponible nuestras tablas - entre parentesis el nombre del modelo
admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)