# Django Rest Framework
# Serializers define the API representation.
from rest_framework.serializers import ModelSerializer
from core.models import Endereco

class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'endereco', 'complemento', 'cidade', 'estado', 'pais', 'latitude', 'longitude', )