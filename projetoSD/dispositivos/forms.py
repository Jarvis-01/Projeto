from django.forms import ModelForm
from . models import Dispositivos

class DispositivosForm(ModelForm):
    class Meta:
        model = Dispositivos
        fields = "__all__"