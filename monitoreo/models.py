from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

from dispositivos.models import Dispositivo, Variable

class Zona(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(default=timezone.now)
	latitud = models.CharField(max_length=100, blank=True, null=True)
	longitud = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)


class Vuelo(models.Model):
	descripcion = models.CharField(max_length=100, blank=True, null=True)
	fecha = models.DateTimeField(default=timezone.now, blank=True, null=True)
	dispositivo = models.ForeignKey(Dispositivo)
	zona = models.ForeignKey(Zona)
	usuario = models.ForeignKey(User, blank=True, null=True)
	def __unicode__(self):
		return '%s' % (self.fecha)

class DataVuelo(models.Model):
	fecha = models.DateTimeField(default=timezone.now)
	latitud = models.CharField(max_length=100, blank=True, null=True)
	longitud = models.CharField(max_length=100, blank=True, null=True)
	altitud = models.CharField(max_length=100, blank=True, null=True)
	vuelo = models.ForeignKey(Vuelo)
	zona = models.ForeignKey(Zona)
	variable = models.ForeignKey(Variable)
	data = models.CharField(max_length=200)
	def __unicode__(self):
		return '%s' % (self.fecha)