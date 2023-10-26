from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path("detalhes/<int:pk>/", views.detalhes, name='detalhes'),
    path('gerarqr/', views.gerarqr, name='gerarqr'),
    path('criar_falha/<int:dispositivo_id>/', views.criar_falha, name='criar_falha'),
]