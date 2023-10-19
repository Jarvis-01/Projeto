
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("detalhes/<int:pk>/", views.detalhes, name='detalhes'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]