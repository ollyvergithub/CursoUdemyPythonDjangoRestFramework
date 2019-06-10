from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao =  models.TextField()
    aprovado = models.BooleanField(default=False)

    #Criando o relacionamento do core com Atracao
    atracoes = models.ManyToManyField(Atracao)
    #Criando o relacionamento do core com Comentario
    comentarios = models.ManyToManyField(Comentario)
    #Criando o relacionamento do core com Avaliacao
    avaliacoes = models.ManyToManyField(Avaliacao)
    #Criando o relacionamento do core com Endereco
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    # 33 - Incluindo informações adicionais com SerializerMethodField e properties
    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome

