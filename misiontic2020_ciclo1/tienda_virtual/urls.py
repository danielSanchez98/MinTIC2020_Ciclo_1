from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('carrito_compras/', views.carrito, name="carrito"),
    path('historial_compras/', views.historial, name="historial"),
    path('productos/', views.productos, name="lista_productos"),
    path('portal_pagos/', views.pagos, name="pagos"),
]