from django.shortcuts import render
from app1.forms import FixosForm, DiarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fixos, Diario
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_cron import CronJobBase, Schedule
from django.utils import timezone
from .models import Notificacao, relacao
from django.contrib.auth.decorators import login_required

from .forms import  RelacaoForm

def about(request):
    return render(request, "about.html", {})

def relacao(request):
    if request.method == 'POST':
        form = RelacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar")
    else:
        form = RelacaoForm()

    return render(request, "app1/dia.html", {"form": form})

class NotificacaoDiariaCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440  # Executar a cada 24 horas (60 minutos x 24 horas)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app1.notificacao_diaria_cron_job'  # Um identificador exclusivo para o cron job

    def do(self):
        notificacao = Notificacao(mensagem="Sua notificação aqui")
        notificacao.save()


def add(request):
    if request.method == 'POST':
        form = DiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar")
    else:
        form = DiarioForm()

    return render(request, "app1/add.html", {"form": form})

def apagar(request, diario_id):
    Diario.objects.filter(id=diario_id).delete()
    return redirect('index')

def mostrar(request):
 
    diario = Diario.objects.all().order_by('-data')
    context = {
        'diario': diario
    }
   
    return render(request, "app1/mostrar.html", context)

def alterar(request, diario_id):
  
    editar = Diario.objects.get(id=diario_id)
    form = DiarioForm(instance=editar)
    if form:
        if request.method == "POST":
                form = DiarioForm(request.POST, request.FILES, instance=editar)
                if form.is_valid():
                    form.save()
                    return redirect('mostrar')
    
    else:
        return redirect('mostrar')
    context = {
            'form': form,
            'editar' : editar
        }
    return render(request, 'app1/alterar.html', context)



@login_required
def index(request):
    return render(request, "index.html", {})

def criar(request):
    if request.method == 'POST':
        form = FixosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("publicar")
    else:
        form = FixosForm()

    return render(request, "app1/criar.html", {"form": form})

def deletar(request, fixos_id):
    Fixos.objects.filter(id=fixos_id).delete()
    return redirect('publicar')

def publicar(request):
    diario = Diario.objects.all().order_by('-data')
    fixos = Fixos.objects.all().order_by('-data')
    context = {
    	'fixos': fixos,
        'diario': diario
    }
   
    return render(request, "app1/publicar.html", context)

def editar(request, fixos_id):
  
    editar = Fixos.objects.get(id=fixos_id)
    form = FixosForm(instance=editar)
    if form:
        if request.method == "POST":
                form = FixosForm(request.POST, request.FILES, instance=editar)
                if form.is_valid():
                    form.save()
                    return redirect('publicar')
    
    else:
        return redirect('publicar')
    context = {
            'form': form,
            'editar' : editar
        }
    return render(request, 'app1/editar.html', context)

