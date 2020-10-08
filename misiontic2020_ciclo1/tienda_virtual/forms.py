from django import forms

class agregar_producto(forms.Form):
    productos = ()
    cantidad = ((i, i) for i in range(10))
    
    producto = forms.ChoiceField(label = "Producto", required=True, choices=productos)
    cantidad = forms.ChoiceField(label = "Cantidad", required=True, choices=cantidad)
    observaciones = forms.CharField(label = "Observaciones", required=False)


class pagar_carrito(forms.Form):
    metodos = (('Tarjeta', 'Tarjeta'), ('Efectivo', 'Efectivo'))

    metodo_pago = forms.ChoiceField(label = "Método de Pago", required=True, choices=metodos)
    direccion = forms.CharField(label = "Dirección", required=False)
    observaciones = forms.CharField(label = "Observaciones", required=False)