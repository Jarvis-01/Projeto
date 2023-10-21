from django.forms import ModelForm
from . models import Falha

class FalhasForm(ModelForm):
    class Meta:
        model = Falha
        fields = "__all__"