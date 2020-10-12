from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inicio"),
    # MINTIC2020 ->  Acá debe colocar el resto de URLs para completar el mapeo de todas las vistas
]