from django.shortcuts import render
# importamos HttpResponse
from django.http import HttpResponse

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

# %r es el request en este caso de buscar producto
def buscar(request):
    if request.GET["prd"]:
        mensaje="Artículo buscado: %r" %request.GET["prd"]
        
    else:
        mensaje="No has introducido ningún producto"
    return HttpResponse(mensaje)