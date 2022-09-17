from django.urls import path
from our_app.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', clientes, name='clientes'),
    path('ropas/', ropas, name='ropas'),
    path('staff/', staff, name='staff'),
    path('envios/', envios, name='envios'),
    path('buscarCliente/', buscarCliente, name="buscarCliente"),
    path('buscar/', find, name="find"),
]
