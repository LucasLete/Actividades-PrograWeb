from django.shortcuts import render, redirect
from .forms import ServicioForm
from .models import Servicio
# Create your views here.


def index(request):
    servicios = Servicio.objects.all()
    context={"servicios":servicios}
    return render(request, 'servicios/index.html', context)

def servicio_create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ServicioForm()
    return render(request, 'servicio_form.html', {'form': form})