
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index2'),
    path("detalhe/<int:pk>/", views.detalhe, name='detalhe'),
    path('adiciona/', views.adicionar, name='adiciona'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),   
]