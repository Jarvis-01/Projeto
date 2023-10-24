import io
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Dispositivos
from . forms import DispositivosForm
import qrcode
from PIL import Image
# Create your views here.
data = ''
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

def gerarqr(request):
    data = request.META.get('HTTP_REFERER', None)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")

    # Salvar o QR code em um objeto de BytesIO
    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")

    # Retornar o QR code como um arquivo de download
    response = HttpResponse(content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
    img_buffer.seek(0)
    response.write(img_buffer.read())

    return response



