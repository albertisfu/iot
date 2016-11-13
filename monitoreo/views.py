
from django.shortcuts import render, redirect, get_object_or_404
from forms import *
from django.utils import timezone
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
import django_filters
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
# Create your views here.

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# AGREGAR NUEVO PRODUCTO

@login_required
def addzona(request):
    current_user = request.user
    form = AltaZona(initial={'usuario':current_user,})
    form.fields['usuario'].widget = forms.HiddenInput()
    if request.method == "POST":
            form = AltaZona(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.fecha = timezone.now()
                post.save()
                return redirect('ver_zonas')
  
    return render(request, 'add_zone.html', {'form': form})


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# LISTAR PRODUCTOS


class verzonas(ListView):

    model = Zona
    template_name = 'list_zones.html'
    paginate_by = 50  # Elementos por pagina


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(verzonas, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        list_prod = Zona.objects.all()
        paginator = Paginator(list_prod, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            file_prod = paginator.page(page)
        except PageNotAnInteger:
            file_prod = paginator.page(1)
        except EmptyPage:
            file_prod = paginator.page(paginator.num_pages)

        context['list_prod'] = file_prod
        return context


@login_required
def zonadetalle(request, pk):
    #paginate_by = 2 # Elementos por pagina
    proddet = get_object_or_404(Zona, pk = pk)
    vuelos = Vuelo.objects.filter(zona=proddet)
    return render(request, 'zona_detail.html', {'proddet': proddet, 'vuelos':vuelos})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# AGREGAR NUEVO Vuelo
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
@login_required
def addvuelo(request, pk):
    zona = get_object_or_404(Zona, pk = pk)
    current_user = request.user
    form = AltaVuelo(initial={'usuario':current_user, 'zona':zona})
    form.fields['usuario'].widget = forms.HiddenInput()
    form.fields['zona'].widget = forms.HiddenInput()
    if request.method == "POST":
            form = AltaVuelo(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.fecha = timezone.now()
                post.save()
                return HttpResponseRedirect(reverse('ver_vuelos', args=(zona.id,)))
  
    return render(request, 'add_vuelo.html', {'form': form})


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# LISTAR Vuelos


@login_required
def vervuelos(request, pk):
    #paginate_by = 2 # Elementos por pagina
    zona = get_object_or_404(Zona, pk = pk)
    vuelos = Vuelo.objects.filter(zona=zona)

    return render(request, 'vuelos_lista.html', {'zona': zona, 'vuelos':vuelos})


@login_required
def vuelodetalle(request, pk):
    #paginate_by = 2 # Elementos por pagina
    proddet = get_object_or_404(Vuelo, pk = pk)
    #print proddet.dispositivo.variables.all()
    return render(request, 'vuelo_detail.html', {'proddet': proddet})


from dispositivos.models import Variable

@login_required
def variablevuelodetalle(request, vuelo, variable):
    #paginate_by = 2 # Elementos por pagina
    vuelo = get_object_or_404(Vuelo, pk = vuelo)
    variable =  get_object_or_404(Variable, pk = variable)
    data =  DataVuelo.objects.filter(vuelo=vuelo, variable=variable)
    try:
        firstdata =  DataVuelo.objects.filter(vuelo=vuelo, variable=variable)[0]
        latitud = firstdata.latitud
        longitud = firstdata.longitud
    except:
        latitud = 19.002631
        longitud = -98.201048


    #print proddet.dispositivo.variables.all()
    return render(request, 'detalle_variable_vuelo.html', {'vuelo': vuelo, 'variable':variable, 'data':data, 'latitud':latitud, 'longitud':longitud})



# Create your views here.

def DatosJsonAdd(request):
    vuelo = request.GET.get('vuelo') 
    var = request.GET.get('var')
    data = request.GET.get('data') 
    lat= request.GET.get('lat') 
    lon= request.GET.get('lon') 
    alt= request.GET.get('alt')   
    if request.method == 'GET':
        idint = int(vuelo)
        idvar = int(var)
        vuelo = get_object_or_404(Vuelo, pk=idint)
        variable = get_object_or_404(Variable, pk=idvar)
        fecha = timezone.now()

        p,created = DataVuelo.objects.get_or_create(vuelo=vuelo, fecha= fecha, variable=variable, data= data, latitud=lat, longitud=lon, altitud=alt)
        if created:
            print 'creado'
            p.save()
        else:
            print 'existe'

    return HttpResponse(200)





