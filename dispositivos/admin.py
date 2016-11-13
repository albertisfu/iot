from django.contrib import admin
from dispositivos.models import *
# Register your models here.

class VariableAdmin(admin.ModelAdmin):
	model = Variable


class DispositivoAdmin(admin.ModelAdmin):
	model = Dispositivo


admin.site.register(Dispositivo, DispositivoAdmin)

admin.site.register(Variable, VariableAdmin)