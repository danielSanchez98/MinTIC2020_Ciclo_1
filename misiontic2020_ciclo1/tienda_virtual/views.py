from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')

def carrito(request):
    productos = []
    return render(request, 'tienda_virtual/carrito_compras.html', {'productos':  productos})

def historial(request):
    historial = []
    return render(request, 'tienda_virtual/historial.html', {'historial':  historial})

def productos(request):
    frm_agregar = forms.agregar_producto()
    return render(request, 'tienda_virtual/lista_productos.html', {'frm_agregar' :  frm_agregar})

def pagos(request):
    frm_pago = forms.pagar_carrito()
    return render(request, 'tienda_virtual/pagar.html', {'frm_pago' :  frm_pago})