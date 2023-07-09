from django_cron import CronJobManager

from django.urls import path

from . import views
from app1.views import NotificacaoDiariaCronJob


urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.about, name="about"),
    path('diario/', views.publicar, name="publicar"),
    path('criar/', views.criar, name="criar"),
    path('mostrar/', views.mostrar, name="mostrar"),
    path('add/', views.add, name="add"),
    path('cron/', views.NotificacaoDiariaCronJob, name="cron"),
    path('editar/<fixos_id>', views.editar, name="editar"),
    path('alterar/<diario_id>', views.alterar, name="alterar"),
    path('excluir/<fixos_id>', views.deletar, name="excluir"),
    path('relacao/', views.relacao, name="relacao"),

 
]