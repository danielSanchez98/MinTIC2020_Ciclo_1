from django.shortcuts import render
from . import forms

from pymongo import MongoClient

# Conexión a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db_tienda_virtual = client.tiendaVirtual


# Create your views here.
def home(request):
    return render(request, 'tienda_virtual/index.html')


def carrito(request):
    productos = []
    cursor = db_tienda_virtual['carrito'].find()
    for document in cursor:
        temp = {}
        temp['nombre'] = document['nombre']
        temp['costo'] = document['costo']
        temp['cantidad'] = document['cantidad']
        productos.append(temp)

    parametros = {'productos':  productos}
    return render(request, 'tienda_virtual/carrito_compras.html', parametros)


def historial(request):
    historial = []
    cursor = db_tienda_virtual['compras'].find()
    for document in cursor:
        temp = {}
        temp['nombre'] = document['productos']
        temp['costo'] = document['costo']
        temp['fecha'] = document['fecha']
        temp['metodo'] = document['metodo']
        temp['direccion'] = document['direccion']
        historial.append(temp)

    parametros = {'historial':  historial}
    return render(request, 'tienda_virtual/historial.html', parametros)


def productos(request):
    productos = []
    cursor = db_tienda_virtual['productos'].find()
    for document in cursor:
        temp = {}
        temp['nombre'] = document['nombre']
        temp['costo'] = document['costo']
        productos.append(temp)
   
    frm_agregar = forms.agregar_producto()
    parametros = {'frm_agregar':  frm_agregar, 'productos': productos}
    return render(request, 'tienda_virtual/lista_productos.html', parametros)


def pagos(request):
    frm_pago = forms.pagar_carrito()
    costo = 0
    
    cursor = db_tienda_virtual['carrito'].find()
    for document in cursor:
        costo += int(document['costo']) * int(document['cantodad'])
    
    parametros = {'frm_pago':  frm_pago, 'costo': costo}
    return render(request, 'tienda_virtual/pagar.html', parametros)