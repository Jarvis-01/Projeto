from datetime import date
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Falha
from .forms import FalhasForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        #copiar os dados enviados
        dados = request.POST.copy()
        #pegar o primeiro item
        ultimaMes = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado', flat=True)[:1][0].month
        ultimaAno = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado', flat=True)[:1][0].year
        primeiraMes = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado', flat=True)[:1][0].month
        primeiraAno = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado', flat=True)[:1][0].year
        inicioMes = int(dados['mes_inicial'])
        inicioAno = int(dados['ano_inicial'])
        fimMes = int(dados['mes_final'])
        fimAno = int(dados['ano_final'])
        falhas = Falha.objects.filter(registro_atualizado__range=(date(inicioAno, inicioMes, 1), date(fimAno, fimMes, 31)))
    else:
        falhas = Falha.objects.all()
        ultimaMes = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado',flat=True)[:1][0].month
        ultimaAno = Falha.objects.order_by('-registro_atualizado').values_list('registro_atualizado',flat=True)[:1][0].year
        primeiraMes = Falha.objects.order_by('registro_atualizado').values_list('registro_atualizado',flat=True)[:1][0].month
        primeiraAno = Falha.objects.order_by('registro_atualizado').values_list('registro_atualizado',flat=True)[:1][0].year
        
    context = {
        'lista': falhas,
        'faixaMes':range(primeiraMes,ultimaMes+1),
        'faixaAno' :range(primeiraAno,ultimaAno+1),
        'ultimaMes': ultimaMes,
        'ultimaAno': ultimaAno,
    }
    return render(request, 'falhas.html', context)

def detalhe(request,pk):
    print("Primary Key {}".format(pk))
    try:
        falhas = Falha.objects.filter(pk=pk)
        print(falhas.values())
        
    except falhas.DoesNotExist:
        raise Http404('Falha Não Existe')
    # consulta
    context = {
        'falhas': falhas
    }
    return render(request, 'detalhe.html', context)

def adicionar(request):
    form = FalhasForm()
    if request.method == "POST":
        form = FalhasForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = FalhasForm()
            return redirect('../')
        else:
            form = FalhasForm()
    return render(request, 'adicionar_dispositivo.html', {'form': form})    

def editar(request, id):
    falhas = get_object_or_404(Falha, pk=id)
    form = FalhasForm(instance=falhas)

    if(request.method == 'POST'):
        form = FalhasForm(request.POST, instance=falhas)

        if(form.is_valid()):
            falhas.save()
            return redirect('../')
        else:
            return render(request, 'editar_falha.html', {'form': form, 'falhas': falhas})

    else:
        return render(request, 'editar_falha.html', {'form': form, 'falhas': falhas})
    
def deletar(request, id):
    falhas = get_object_or_404(Falha, pk=id)
    falhas.delete()
    return redirect('../')