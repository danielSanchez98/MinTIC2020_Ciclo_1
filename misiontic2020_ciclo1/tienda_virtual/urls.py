from django.conf.urls import url
from . import views

url_patterns = [
    url(r'^$', views.home, name="inicio"),
    url(r'^carrito_compras/$', views.carrito, name="carrito"),
    url(r'^historial_compras/$', views.historial, name="historial"),
    url(r'^productos/$', views.productos, name="lista_productos"),
    url(r'^portal_pagos/$', views.pagos, name="pagos"),
]