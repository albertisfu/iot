# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey 


#generar clave activacion
import uuid

#Correo
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User, Permission, Group

def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return 'user_{0}/{1}'.format(instance.user.id, filename)

def user_directoryfile_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return 'user_{0}/files/{1}'.format(instance.user.id, filename)


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	edad = models.IntegerField(blank=True, null=True)
	telefono = models.CharField(max_length=15, blank=True, null=True)
	celular = models.CharField(max_length=15, blank=True, null=True)
	sexo_options = (
		(1, 'Hombre'),
		(2, 'Mujer'),
		)
	sexo = models.IntegerField(choices=sexo_options, blank=True, null=True)
	direccion = models.TextField(max_length=100, blank=True, null=True)
	descripcion = models.TextField(max_length=200, blank=True, null=True)
	email_verif = models.BooleanField(default=False)
	primera_visita = models.BooleanField(default=True)

	def __unicode__(self):
		return '%s' % (self.user)

	class Meta:
		verbose_name_plural = "Perfiles"


class Activar_cuenta(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	clave = models.CharField(max_length=40, null=True, blank=True)
	uso = models.BooleanField(default=False)
	email = models.EmailField(null=True, blank=True)


# ------------------------------------------------------
# Crear perfil cuando se crea usuario y enviar email de verificacion
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(user=instance)
		activacionrandom = str(uuid.uuid4())
		activacionrandom = activacionrandom.replace("-","")
		activacionrandom = activacionrandom[0:30]
		Activar_cuenta.objects.create(user=instance, clave=activacionrandom, email=instance.email)
		subject = 'Verificar email'
		from_email = settings.EMAIL_SALIDA
		to_email = [instance.email]
		message_email = "Verifica tu email! Da clic en el siguiente enlace: \ http://3ce476da.ngrok.io/usuario/activar/%s/%s" % (activacionrandom, instance.email)
		send_mail(subject, message_email, from_email, to_email, fail_silently=True)