# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from models import *
from django import forms
from ckeditor.widgets import CKEditorWidget



class Usuarioform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class Perfilform(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('edad', 'telefono', 'celular', 'sexo',
        'direccion', 'descripcion')