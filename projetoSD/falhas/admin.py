from django.contrib import admin

from .models import Falha
# Register your models here.
class FalhaAdmin(admin.ModelAdmin):
    readonly_fields = ["registro_criado", "registro_atualizado"]

admin.site.register(Falha, FalhaAdmin)


