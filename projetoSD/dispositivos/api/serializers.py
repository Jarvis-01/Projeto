from rest_framework import serializers
from dispositivos import models

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dispositivos
        fields = '__all__'