from django import forms
from pymongo import MongoClient

class agregar_producto(forms.Form):
    client = MongoClient('mongodb://localhost:27017/')
    db_tienda_virtual = client.tiendaVirtual
    
    cursor = db_tienda_virtual['productos'].find()
    productos = ((document['nombre'], document['costo']) for document in cursor)
    cantidad = ((i, i) for i in range(16))
    
    producto = forms.ChoiceField(label = "Producto", required=True, choices=productos)
    cantidad = forms.ChoiceField(label = "Cantidad", required=True, choices=cantidad)


class pagar_carrito(forms.Form):
    metodos = (('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('Pago en Efectivo', 'Pago en Efectivo'), ('Tarjeta Débito', 'Tarjeta Débito'))

    metodo_pago = forms.ChoiceField(label = "Método de Pago", required=True, choices=metodos)
    direccion = forms.CharField(label = "Dirección de Envío", required=True)
    observaciones = forms.CharField(label = "Observaciones", required=False)