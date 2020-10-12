from django.shortcuts import render
from . import forms


def home(request):
    '''
    Esta función indica la carga de la pantalla de Inicio de la Tienda Virtual
    '''
    return render(request, 'tienda_virtual/index.html')


def carrito(request):
    '''
    Esta función indica la carga de la pantalla en la cual se visualiza el actual carrito de compras en la Tienda Virtual
    '''
    # MINTIC2020 ->  Acá debe colocar la variable que corresponde a la lista de productos en el carrito
    # MINTIC2020 ->  Acá debe crear los parámetros a enviar al HTML
    # MINTIC2020 ->  Acá debe hacer el return y render correspondiente para la función de la vista


def historial(request):
    '''
    Esta función indica la carga de la pantalla en la cual se podrá visualizar el historial de compras de la Tienda Virtual
    '''
    # MINTIC2020 ->  Acá debe colocar la variable que corresponde a la lista de compras registrada
    # MINTIC2020 ->  Acá debe crear los parámetros a enviar al HTML
    # MINTIC2020 ->  Acá debe hacer el return y render correspondiente para la función de la vista


def productos(request):
    '''
    Esta función indica la carga de la pantalla que tiene el listado de productos que pueden ser agregados al carrito de la Tienda Virtual
    '''
    # MINTIC2020 ->  Acá debe colocar la variable que corresponde a la lista de productos en la base de datos
    
    # MINTIC2020 ->  Acá se debe invocar al formulario para agregar un producto al carrito
    # MINTIC2020 ->  Acá debe crear los parámetros a enviar al HTML
    # MINTIC2020 ->  Acá debe hacer el return y render correspondiente para la función de la vistareturn render(request, 'tienda_virtual/lista_productos.html', parametros) # MINTIC2020 ->  Acá se deben relacionar las URLs de la aplicación


def pagos(request):
    '''
    Esta función indica la carga de la pantalla en la cual se realiza el Pago de los productos que estén en el carrito de la Tienda Virtual
    '''
    # MINTIC2020 ->  Acá se debe invocar al formulario para realizar el pago
    # MINTIC2020 ->  Acá se debe colocar la variable que acumulara el costo total del pago a realizar
    
    # MINTIC2020 ->  Acá debe crear los parámetros a enviar al HTML
    # MINTIC2020 ->  Acá debe hacer el return y render correspondiente para la función de la vistareturn render(request, 'tienda_virtual/lista_productos.html', parametros) # MINTIC2020 ->  Acá se deben relacionar las URLs de la aplicación
