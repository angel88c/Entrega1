from django.shortcuts import render
from django.http import HttpResponse
from our_app.forms import ClienteForm, RopaForm, StaffForm, EnvioForm
from .models import *

# Create your views here.
def clientes(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        print(form_cliente)
        if form_cliente.is_valid:
            info = form_cliente.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
            cliente.save()

            return render(request, 'our_app/inicio.html')
    else:
        formulario = ClienteForm()
        return render(request, 'our_app/clientes.html', {'formulario': formulario})

def inicio(request):
    return render(request, 'our_app/inicio.html')

def ropas(request):
    if request.method == "POST":
        form_ropa = RopaForm(request.POST)
        print(form_ropa)
        if form_ropa.is_valid:
            info = form_ropa.cleaned_data
            descripcion = info["descripcion"]
            precio = info["precio"]
            prenda = Ropa(descripcion=descripcion, precio=precio)
            prenda.save()
            return render(request, 'our_app/inicio.html')
    else:
        formulario = RopaForm()
        return render(request, 'our_app/ropas.html', {'formulario': formulario})

def staff(request):
    if request.method == "POST":
        form_staff = StaffForm(request.POST)
        print(form_staff)
        if form_staff.is_valid:
            info = form_staff.cleaned_data
            nombre= info["nombre"]
            apellido=info["apellido"]
            email = info["email"]
            profesion =info["profesion"]
            persona_staff = Staff(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            persona_staff.save()
            return render(request, 'our_app/inicio.html')
    else:
        formulario = StaffForm()
        return render(request, 'our_app/staff.html', {'formulario': formulario})

def envios(request):
    if request.method == "POST":
        form_envio = EnvioForm(request.POST)
        print(form_envio)
        if form_envio.is_valid:
            info = form_envio.cleaned_data
            print(info)
            nombre= info["nombre"]
            fecha_entrega=info["fecha_entrega"]
            entregado = info["entregado"]

            envio = Envio(nombre=nombre, fecha_entrega=fecha_entrega, entregado=entregado)
            envio.save()
            return render(request, 'our_app/inicio.html')
    else:
        formulario = EnvioForm()
        return render(request, 'our_app/envios.html', {'formulario': formulario})

"""Busquedas"""
def buscarCliente(request):
    return render(request, 'our_app/buscarCliente.html')

def find(request):
    nombre = request.GET["nombre"]

    if nombre:
        clientes = Cliente.objects.filter(nombre__contains=nombre)

        return render(request, "our_app/resultadosBuscarCliente.html", {"clientes": clientes})
    else:
        mensaje = f"Por favor ingrese un nombre de cliente."
        return render(request, "our_app/buscarCliente.html", {"mensaje": mensaje})