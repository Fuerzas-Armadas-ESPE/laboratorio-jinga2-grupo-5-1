from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
            return render(request, 'listar.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'formulario': form})