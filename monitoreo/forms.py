
# -*- coding: utf-8 -*-
from django import forms
from models import *


class AltaZona(forms.ModelForm):
    class Meta:
        model = Zona
        #localized_fields = ('__all__')
        fields = ('usuario','nombre', 'descripcion')
        labels = {
            'nombre': ('Nombre de la zona'),
            'descripcion': ('Descripción de la zona'),
            }
        widgets = {
            'descripcion': forms.TextInput(),
        }



class AltaVuelo(forms.ModelForm):
    class Meta:
        model = Vuelo
        #localized_fields = ('__all__')
        fields = ('descripcion','dispositivo','zona', 'usuario')




