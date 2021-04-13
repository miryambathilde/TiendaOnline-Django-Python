from django.contrib import admin
#importacion de tabla clientes desde el archivo gestionPedidos-models.py
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno")
    search_fields=("nombre", "tfno")
        
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion")
#linea de codigo para tener desde el admin disponible nuestras tablas - entre parentesis el nombre del modelo
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos)