from django.shortcuts import render
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from .forms import AccountsForm
from django.shortcuts import redirect
# Create your views here.

def UsuarioCreate(request):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            user = form.save() #salva o formulario de usuario
          
            return redirect('login') # retorna para a página de login
    else:
        form = AccountsForm()
    return render(request, "registration/register.html", {'form': form}) 


