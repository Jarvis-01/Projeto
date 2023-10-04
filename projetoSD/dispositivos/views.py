from django.shortcuts import render
from . models import Dispositivos
from . forms import DispositivosForm

# Create your views here.
def index(request):
    dispositivos = Dispositivos.objects.all()
    context = {
        'lista': dispositivos
    }
    return render(request, 'dispositivos.html', context)

def adicionar(request):
    form = DispositivosForm()
    if request.method == "POST":
        form = DispositivosForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = DispositivosForm()
            return render(request, 'adicionar_dispositivo.html', {'form': form})
        else:
            form = DispositivosForm()
    return render(request, 'adicionar_dispositivo.html', {'form': form})