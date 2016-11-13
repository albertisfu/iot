from django.contrib import admin
from monitoreo.models import *
# Register your models here.

class ZonaAdmin(admin.ModelAdmin):
	model = Zona

admin.site.register(Zona, ZonaAdmin)


class VueloAdmin(admin.ModelAdmin):
	model = Vuelo


admin.site.register(Vuelo, VueloAdmin)

class DataVueloAdmin(admin.ModelAdmin):
	model = DataVuelo


admin.site.register(DataVuelo, DataVueloAdmin)