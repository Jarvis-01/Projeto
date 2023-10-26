from django import forms
from django.forms import ModelForm
from . models import Dispositivos
from falhas.models import Falha

class DispositivosForm(ModelForm):
    class Meta:
        model = Dispositivos
        fields = "__all__"

class FalhaForm(forms.ModelForm):
    class Meta:
        model = Falha
        fields = ['titulo', 'detalhes', 'equipamento']
        widgets = {'equipamento': forms.HiddenInput()}