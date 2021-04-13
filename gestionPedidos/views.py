from django.shortcuts import render
# importamos HttpResponse
from django.http import HttpResponse

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

# %r es el request
def buscar(request):
    mensaje="Artículo buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)