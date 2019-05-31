# Django Rest Framework
# Serializers define the API representation.
from rest_framework.serializers import ModelSerializer
from core.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id','user','comentario','nota','data',)