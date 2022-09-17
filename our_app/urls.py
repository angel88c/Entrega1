from django.urls import path
from our_app.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', clientes, name='clientes'),
    path('ropas/', ropas, name='ropas'),
    path('staff/', staff, name='staff'),
    path('envios/', envios, name='envios'),
   # path('busquedaComision/', busquedaComision, name="busquedaComision"),
   # path('buscar/', buscar, name="buscar"),
]
