# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 22:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activar_cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(blank=True, max_length=40, null=True)),
                ('uso', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('sexo', models.IntegerField(blank=True, choices=[(1, 'Hombre'), (2, 'Mujer')], null=True)),
                ('direccion', models.TextField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=200, null=True)),
                ('email_verif', models.BooleanField(default=False)),
                ('primera_visita', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
