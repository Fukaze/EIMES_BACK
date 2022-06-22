from django.contrib import admin
from .models import Marca,Modelo,Equipo_instance,Certificado

# Register your models here.

admin.site.register(Equipo_instance)
admin.site.register(Certificado)
admin.site.register(Marca)
admin.site.register(Modelo)