from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario


# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao =  models.TextField()
    aprovado = models.BooleanField(default=False)

    #Criando o relacionamento do core com Atracao
    atracoes = models.ManyToManyField(Atracao)
    #Criando o relacionamento do core com Comentario
    comentarios = models.ManyToManyField(Comentario)



    def __str__(self):
        return self.nome

