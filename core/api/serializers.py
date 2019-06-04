# Django Rest Framework
# Serializers define the API representation.
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id','nome', 'descricao', 'aprovado')