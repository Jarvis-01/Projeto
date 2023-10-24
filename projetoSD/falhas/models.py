from django.db import models
from dispositivos.models import Dispositivos

# Create your models here.
class Falha(models.Model):
    titulo = models.CharField(max_length=250)

    equipamento = models.ForeignKey(Dispositivos, on_delete=models.CASCADE, null=True, blank=True, related_name="equipamento")

    st = {
        ("F", "Funcionando"),
        ("D", "Defeito"),
        ("R", "Reparação"),
    }
    status_dispositivo = models.CharField(max_length=30, choices=st, default="D")

    registro_criado = models.DateField(auto_now_add=True, null=True, blank=True)

    registro_atualizado = models.DateField(auto_now=True, null=True, blank=True)

    detalhes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo