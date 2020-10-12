from django import forms


class agregar_producto(forms.Form):
    # MINTIC2020 ->  Colocar acá la tupla de posibles productos a agregar
    # MINTIC2020 ->  Colocar acá la tupla de cantidad de elementos a agregar
    
    # MINTIC2020 ->  Agregar componente desplegable para los productos a mostrar
    # MINTIC2020 ->  Agregar componente desplegable para la cantidad de productos a llevar

    
class pagar_carrito(forms.Form):
    # MINTIC2020 ->  Colocar acá la tupla de métodos de pago

    # MINTIC2020 ->  Agregar componente desplegable para los métodos de pago
    # MINTIC2020 ->  Agregar componente de texto para colocar el nombre
    # MINTIC2020 ->  Agregar componente de texto para colocar la dirección
    # MINTIC2020 ->  Agregar componente de texto para colocar las observaciones