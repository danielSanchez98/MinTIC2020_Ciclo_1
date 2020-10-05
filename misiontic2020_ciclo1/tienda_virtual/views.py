from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')

def carrito(request):
    return render(request, 'tienda_virtual/carrito_compras.html')

def historial(request):
    return render(request, 'tienda_virtual/historial.html')

def productos(request):
    return render(request, 'tienda_virtual/lista_productos.html')

def pagos(request):
    return render(request, 'tienda_virtual/pagar.html')