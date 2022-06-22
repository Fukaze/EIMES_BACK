"""
    num_marcas = 1
    num_instances = 2

    num_instances_electrico = 3
    num_instances_omicron = 4

    num_modelos = 5
"""

from django.shortcuts import render
#IMPORTA MODELOS PARA ACCEDER A ELLOS A LEER O SACAR INFO
from .models import Marca,Modelo, Equipo_instance, Certificado
# Create your views here.

def index(request):

    num_marcas = Marca.objects.all().count()
    num_instances = Equipo_instance.objects.all().count()

    num_instances_electrico = Equipo_instance.objects.filter(tipo='e').count()
    num_instances_omicron = Equipo_instance.objects.filter(modelo__nombre__exact='cmc355').count()

    num_modelos = Modelo.objects.count()

    context = {
        'num_marcas': num_marcas,
        'num_instances': num_instances,
        'num_instances_electrico': num_instances_electrico,
        'num_instances_omicron': num_instances_omicron,
        'num_modelos': num_modelos,
    }
    graba_Marca()
    return render(request, 'index.html', context=context)

def graba_Marca():
    record = Marca(nombre='DELTA REC')
    record.save()
    pass