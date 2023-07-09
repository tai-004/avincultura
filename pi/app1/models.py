from django.db import models
from django.conf import settings


#lote/tipo
class Fixos(models.Model):

    nome = models.CharField(max_length=100, null=True)
    raca= models.CharField(max_length = 254, null=True, blank=True)
    qntI= models.CharField(max_length = 254, null=True, blank=True)
    qntF= models.CharField(max_length = 254, null=True, blank=True)
    mortes= models.CharField(max_length = 254, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return self.nome
 
#dia
class Diario(models.Model):
    CHOICES = (
        ('sim', 'Sim'),
        ('nao', 'Não')
    
    )
    fixos  = models.ManyToManyField(Fixos)
    maiorTemperatura = models.CharField(max_length=100, null=True)
    menorTemperatura= models.CharField(max_length = 254, null=True, blank=True)
    maiorHumidade= models.CharField(max_length = 254, null=True, blank=True)
    menorHumidade= models.CharField(max_length = 254, null=True, blank=True)
    racao= models.CharField(max_length=8, choices=CHOICES, null=True, blank=True)
    tipoQnt = models.CharField(max_length = 254, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)



    def __str__(self):
       return self.data


#diario
class relacao(models.Model):
   
    diario  = models.ForeignKey(Diario, on_delete=models.CASCADE, related_name='diario')
    fixos  = models.ManyToManyField(Fixos)
    text = models.CharField(max_length = 254, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)



    def __str__(self):
       return self.data

class Notificacao(models.Model):
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)