
# -*- coding: utf-8 -*-
from django import forms
from models import *





class AltaVariable(forms.ModelForm):
    class Meta:
        model = Variable
        #localized_fields = ('__all__')
        fields = ('nombre','unidad')
        labels = {
            'nombre': ('Nombre de la variable'),
            'unidad': ('Unidad de la variable'),
            }
        



class Altadispositivo(forms.ModelForm):
    class Meta:
        model = Dispositivo
        #localized_fields = ('__all__')
        fields = ('ide','nombre', 'descripcion', 'usuario', 'variables')
        labels = {
            'nombre': ('Nombre del dispositivo'),
            'ide': ('ID'),
            }
        widgets = {
            'descripcion': forms.TextInput(),
        }


