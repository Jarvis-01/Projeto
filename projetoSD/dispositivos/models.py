from django.db import models

# Create your models here.

class Dispositivos(models.Model):
    nome = models.CharField(max_length=200)
    id_automatico = models.AutoField(primary_key=True)
    sala = models.IntegerField(null=True)
    referencia = models.CharField(max_length=200, null=True)

    #st = {
    #    ("F", "Funcionando"),
    #    ("D", "Defeito"),
    #    ("R", "Reparação"),
    #}

    #status_dispositivo = models.CharField(max_length=30, choices=st, default="F")


    #lattes = models.URLField(max_length=200, null=True, blank=True)
    #google_scholar = models.URLField(max_length=200, null=True, blank=True)
    #research_gate = models.URLField(max_length=200, null=True, blank=True)
    #linkedin = models.URLField(max_length=200, null=True, blank=True)
    #orcid = models.URLField(max_length=200, null=True, blank=True)
    #github = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome