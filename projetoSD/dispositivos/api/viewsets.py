from rest_framework import viewsets
from dispositivos.api import serializers
from dispositivos import models

class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DispositivoSerializer
    queryset = models.Dispositivos.objects.all()