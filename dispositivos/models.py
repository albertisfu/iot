from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here. 

class Variable(models.Model):
	nombre = models.CharField(max_length=200)
	unidad = models.CharField(max_length=50)
	def __unicode__(self):
		return '%s' % (self.nombre)


class Dispositivo(models.Model):
	ide = models.CharField(max_length=100, blank=True, null=True)
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=1000, blank=True, null=True)
	usuario = models.ForeignKey(User)
	variables = models.ManyToManyField(Variable, blank=True)
	def __unicode__(self):
		return '%s' % (self.nombre)
