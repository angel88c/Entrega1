from django import forms

class ClienteForm(forms.Form):
    nombre  = forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email   = forms.EmailField()

class RopaForm(forms.Form):
    descripcion = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class StaffForm(forms.Form):
    nombre   = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email    = forms.EmailField()
    profesion= forms.CharField(max_length=50)

class EnvioForm(forms.Form):
    nombre       = forms.CharField(max_length=50)
    fecha_entrega= forms.DateField()
    entregado    = forms.BooleanField()

