from django import forms
from .models import Fixos, Diario, relacao
from django.forms.widgets import FileInput



class FixosForm(forms.ModelForm):
     class Meta:
        model = Fixos
        fields =  ('nome', 'raca', 'qntI', 'qntF', 'mortes')




class DiarioForm(forms.ModelForm):
     class Meta:
        model = Diario
        fields =  ('fixos','maiorTemperatura', 'menorTemperatura', 'maiorHumidade', 'menorHumidade', 'racao', 'tipoQnt')


class RelacaoForm(forms.ModelForm):
     class Meta:
        model = relacao
        fields =  ('text', 'fixos')


    
