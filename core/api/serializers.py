# Django Rest Framework
# Serializers define the API representation.
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer

class PontoTuristicoSerializer(ModelSerializer):
    # Aula 9 - 32 - Incrementando um objeto com NestedRelationships
    # Aqui um relacionamento de muitos para muitos - many=True
    atracoes = AtracoesSerializer(many=True)
    # Aqui um relacionamento simples
    enderecos = EnderecosSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id','nome', 'descricao', 'aprovado', 'foto',
                  'enderecos', 'atracoes', 'comentarios', 'avaliacoes')