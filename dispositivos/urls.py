from django.conf.urls import url, include
from dispositivos import views
from dispositivos.views import verdispositivos

urlpatterns = [

url(r'^dispositivos/dispositivos/$', verdispositivos.as_view(), name='ver_dispositivos'),
    url(r'^dispositivos/agregar_dispositivo/$', views.adddispositivo, name="agregar_dispositivo"),
        url(r'^dispositivos/detalle_dispositivo/(?P<pk>[0-9]+)/$', views.dispositivodetalle, name='detalle_dispositivo'),

   
]