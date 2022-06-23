from django.urls import path
from . import views

urlpatterns = [
        #URL Pattern, view function,                        identifier parameter for reverse mapping
    path('',           views.index,                         name='index'),
    path('Modelos/',    views.ListaModelosView.as_view(),    name = 'modelos'),
    path('Equipo/<int:pk>', views.DetalleEquiposView.as_view(), name = 'detalleEquipo'),
]
