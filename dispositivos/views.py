
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
def adddispositivo(request):
    current_user = request.user
    form = Altadispositivo(initial={'usuario':current_user,})
    form.fields['usuario'].widget = forms.HiddenInput()
    if request.method == "POST":
            form = Altadispositivo(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                form.save_m2m()
                return redirect('ver_dispositivos')
  
    return render(request, 'add_dispositivo.html', {'form': form})


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
# LISTAR PRODUCTOS


class verdispositivos(ListView):

    model = Dispositivo
    template_name = 'list_dispositivo.html'
    paginate_by = 50  # Elementos por pagina


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(verdispositivos, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        list_prod = Dispositivo.objects.all()
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
def dispositivodetalle(request, pk):
    #paginate_by = 2 # Elementos por pagina
    proddet = get_object_or_404(Dispositivo, pk = pk)
    print proddet.variables
    return render(request, 'dispositivo_detail.html', {'proddet': proddet})

