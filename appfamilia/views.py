from django.shortcuts import render
from django.http import HttpResponse
from appfamilia.models import Familia
# Create your views here.
def familiar(request, dni, nombre, apellido, email, fecha_nacimiento):

    
    familia = Familia(dni, nombre, apellido, email, fecha_nacimiento)
    familia.save()
    documento = f" DNI: {familia.dni}  Nombre:{familia.nombre}  Apellido: {familia.apellido}  EMAIL: {familia.email} Fecha Nacimiento: {familia.fecha_nacimiento}" 
    return HttpResponse(documento)


def inicio(request):
   return render(request, "appfamilia/inicio.html")
  
def per(request):
   return render(request, "appfamilia/personas.html")

