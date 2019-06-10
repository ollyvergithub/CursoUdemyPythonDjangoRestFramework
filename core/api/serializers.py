# Django Rest Framework
# Serializers define the API representation.
from rest_framework.fields import SerializerMethodField
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
    # 33 - Incluindo informações adicionais com SerializerMethodField e properties
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id','nome', 'descricao', 'aprovado', 'foto',
                  'enderecos', 'atracoes', 'comentarios', 'avaliacoes',
                  'descricao_completa', 'descricao_completa2')

    # 33 - Incluindo informações adicionais com SerializerMethodField e properties
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)


