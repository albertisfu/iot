from django.conf.urls import url, include
from monitoreo import views
from monitoreo.views import verzonas

urlpatterns = [

url(r'^monitoreo/zonas/$', verzonas.as_view(), name='ver_zonas'),
    url(r'^monitoreo/agregar_zona/$', views.addzona, name="agregar_zona"),
        url(r'^monitoreo/detalle_zona/(?P<pk>[0-9]+)/$', views.zonadetalle, name='detalle_zona'),

   

   url(r'^monitoreo/zona_vuelos/(?P<pk>[0-9]+)/$', views.vervuelos, name='ver_vuelos'),
   url(r'^monitoreo/agregar_vuelo/(?P<pk>[0-9]+)/', views.addvuelo, name="agregar_vuelo"),
   url(r'^monitoreo/detalle_vuelo/(?P<pk>[0-9]+)/$', views.vuelodetalle, name='detalle_vuelo'),

url(r'^monitoreo/detalle_variable/(?P<vuelo>[0-9]+)/(?P<variable>[0-9]+)/$', views.variablevuelodetalle, name='varvuelodetalle'),
url(r'^datosadd/$', views.DatosJsonAdd, name='DatosJsonAdd'), 
]