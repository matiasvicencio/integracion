from django.shortcuts import render, redirect
from . models import producto
def productos(request):
    productolist = producto.objects.all()
    return render(request, 'productos.html', {"producto": productolist})


def agregarproducto(request):
    nombre=request.POST['nombreproducto']
    precio=request.POST['precioproducto']


    nuevo_producto = producto.objects.create(
        nombre=nombre, precio=precio) 
    
    return redirect('/')
