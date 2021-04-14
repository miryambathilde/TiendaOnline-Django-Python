from django.shortcuts import render
# importamos HttpResponse
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

# %r es el request en este caso de buscar producto
def buscar(request):
    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        #variable producto para consulta PRD QUE ES PRODUCTO
        producto=request.GET["prd"]
        #icontains funciona como el like dentro de una consulta de una instruccion SQL, nos devuelve cualquier valor que contenga el nombre del producto sea en la posición que sea
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        #redigir al html que muestre la información del producto buscado
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query":producto})
        
    else:
        mensaje="No has introducido ningún producto"
    return HttpResponse(mensaje)