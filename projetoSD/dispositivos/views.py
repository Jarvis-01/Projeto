from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
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
            return redirect('../')
        else:
            form = DispositivosForm()
    return render(request, 'adicionar_dispositivo.html', {'form': form})

def editar(request, id):
    dispositivos = get_object_or_404(Dispositivos, pk=id)
    form = DispositivosForm(instance=dispositivos)

    if(request.method == 'POST'):
        form = DispositivosForm(request.POST, instance=dispositivos)

        if(form.is_valid()):
            dispositivos.save()
            return redirect('../')
        else:
            return render(request, 'editar_dispositivo.html', {'form': form, 'dispositivos': dispositivos})

    else:
        return render(request, 'editar_dispositivo.html', {'form': form, 'dispositivos': dispositivos})
    
def deletar(request, id):
    dispositivos = get_object_or_404(Dispositivos, pk=id)
    dispositivos.delete()
    return redirect('../')


def detalhes(request,pk):
    try:
        dispositivos = Dispositivos.objects.filter(pk=pk)
        print(dispositivos.values())
        
    except dispositivos.DoesNotExist:
        raise Http404('Dispositivo Não Existe')
    # consulta
    context = {
        'dispositivos': dispositivos
    }
    return render(request, 'detalhes.html', context)