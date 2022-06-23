from concurrent.futures.process import _threads_wakeups
from contextlib import nullcontext
from sys import maxsize
from unicodedata import name
from django.db import models
from django.forms import CharField, FileField
from django.urls import reverse

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50, help_text='Nombre Marca')
    #modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=False)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100, help_text='Nombre Modelo')
    descripcion = models.TextField(max_length=1000, help_text='Descripción del Equipo')
    marca = models.ForeignKey('Marca', on_delete=models.RESTRICT, null=True)
    imagen = models.ImageField(null=True, blank=True)
    manual = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
    
        return reverse('detalle-equipo',args=[str(self.id)])

class Equipo_instance(models.Model):
    modelo = models.ForeignKey('Modelo', on_delete=models.RESTRICT,help_text='Representación Equipo Real')
    #Exige q todo equipo tenga código EIMES
    cod_EIMES = models.CharField(max_length=11, unique=True, null=True)
    #Exige q todo equipo tenga QR
    cod_QR = models.CharField(max_length=50,unique=True,null=False)
    #NO exige q todo equipo tenga QR
    serie = models.CharField(max_length=50,unique=False,null=False)

    tipos = (('e','Eléctrico'),('i','Instrumentación'),('m','Mecánico'),('o','Otros'))

    tipo = models.CharField(max_length=1,choices=tipos,help_text='Categoría del Equipos')

    descripcion_corta = models.CharField(max_length = 50, blank=True)
    descripcion_larga = models.CharField(max_length = 1000, blank=True)
    certif = models.ForeignKey('Certificado', on_delete=models.SET_NULL, blank=True, null=True)
    nro_maletas = models.IntegerField(null=True, blank=True)
    proveedor = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.cod_EIMES

class Certificado(models.Model):
    equipo = models.ForeignKey('Equipo_instance',on_delete=models.SET_NULL, null=True)
    estatus = ((1,'Vigente'),(0,'Vencido'))
    estado = models.IntegerField(choices=estatus)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    archivo = models.FileField(blank=True)
    proveedor = models.CharField(max_length=50)
    def __str__(self):
        return self.equipo.cod_EIMES + ' / ' + str(self.fecha_inicio)