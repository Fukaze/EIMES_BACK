from django.urls import path
from . import views

urlpatterns = [
        #URL Pattern, view function, identifier parameter for reverse mapping
    path('',           views.index,   name='index')
]
