from django import forms

class agregar_producto(forms.Form):
    productos = ()
    cantidad = ((i, i) for i in range(16))
    
    producto = forms.ChoiceField(label = "Producto", required=True, choices=productos)
    cantidad = forms.ChoiceField(label = "Cantidad", required=True, choices=cantidad)


class pagar_carrito(forms.Form):
    metodos = (('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('Pago en Efectivo', 'Pago en Efectivo'), ('Tarjeta Débito', 'Tarjeta Débito'))

    metodo_pago = forms.ChoiceField(label = "Método de Pago", required=True, choices=metodos)
    direccion = forms.CharField(label = "Dirección de Envío", required=True)
    observaciones = forms.CharField(label = "Observaciones", required=False)