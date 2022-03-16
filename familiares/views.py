
from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import date, datetime


listado = []
def carga(request, nombre, apellido):
    
    nombre = nombre
    apellido = apellido 
    nomyape = nombre + " " + apellido       
    listado.append(nomyape)  




    #Dicccionario con los datos que enviamos como contexto
    dict_context = {"nombre": nombre, "apellido": apellido, "listado":listado}

    plantilla = loader.get_template("carga.html")
    documento = plantilla.render(dict_context)
    return HttpResponse(documento)