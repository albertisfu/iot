# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from forms import *
from models import *
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.conf import settings
from django.views.generic import ListView, DeleteView, CreateView
from django.core.urlresolvers import reverse
import json

# Paginacion
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Permisos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Permission, Group


@login_required
def home(request):
	return render(request, 'inicio.html', {'ent': True})

# ---------------------------------------------------------
# ---------------------------------------------------------
#Grupos, checar si pertenece a grupo

def group_required(*group_names):
	def check(user):
		if user.groups.filter(name__in=group_names).exists() | user.is_superuser:
			return True
		else:
			return False
	return user_passes_test(check, login_url='/prohibido/')

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Actualizar cuenta
@login_required
@transaction.atomic
def actualizar_cuenta(request):
	if request.method == 'POST':
		user_form = Usuarioform(request.POST, instance=request.user)
		if user_form.is_valid():
					user_form.save()
					messages.success(request, 'Perfil actualizado')
					print 'actualizado'
					return redirect('actualizar_cuenta')

		else:
			messages.error(request, 'Hay errores.')
	else:
		user_form = Usuarioform(instance=request.user)

	return render(request, 'editar_cuenta.html', {
		'user_form': user_form,
	})


# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Configuraciones usuario

@login_required
def configuraciones_usuario(request):
	usuario = User.objects.get(pk=request.user.id)
	perfil = Perfil.objects.get(user=request.user.id)

	return render(request, 'configuracion_usuario.html', {'usuario':usuario, 'perfil':perfil})

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Actualizar cuenta
@login_required
@transaction.atomic
def actualizar_cuenta(request):
	if request.method == 'POST':
		user_form = Usuarioform(request.POST, instance=request.user)
		if user_form.is_valid():
					user_form.save()
					messages.success(request, 'Perfil actualizado')
					print 'actualizado'
					return redirect('configuraciones_usuario')

		else:
			messages.error(request, 'Hay errores.')
	else:
		user_form = Usuarioform(instance=request.user)

	return render(request, 'editar_cuenta.html', {
		'user_form': user_form,
	})

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Actualizar perfil
@login_required
@transaction.atomic
def actualizar_perfil(request):
	perfil = Perfil.objects.get(user=request.user.id)
	profile_form = Perfilform(request.POST, instance=perfil)
	if request.method == 'POST':
		profile_form = Perfilform(request.POST, instance=perfil)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, 'Perfil actualizado')
			print 'actualizado'
			return redirect('configuraciones_usuario')

		else:
			messages.error(request, 'Hay errores.')
	else:
		profile_form = Perfilform(instance=perfil)

	return render(request, 'editar_perfil.html', {
		'profile_form': profile_form
	})




