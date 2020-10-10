from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')

def carrito(request):
    productos = []
    parametros = {'productos':  productos}
    return render(request, 'tienda_virtual/carrito_compras.html', parametros)

def historial(request):
    historial = []
    parametros = {'historial':  historial}
    return render(request, 'tienda_virtual/historial.html', parametros)

def productos(request):
    frm_agregar = forms.agregar_producto()
    parametros = {'frm_agregar':  frm_agregar}
    return render(request, 'tienda_virtual/lista_productos.html', parametros)

def pagos(request):
    frm_pago = forms.pagar_carrito()
    costo = 0
    parametros = {'frm_pago':  frm_pago, 'costo': costo}
    return render(request, 'tienda_virtual/pagar.html', parametros)