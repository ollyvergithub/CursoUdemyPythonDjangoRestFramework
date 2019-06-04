# Django Rest Framework
# ViewSets define the view behavior.
"""
A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
"""
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    # Com a chamada do método get_queryset
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    # Sobescrevendo o método get_queryset. Aqui filtramos e retornamos um iterable
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # Sobescrevendo o método list() do ModelViewSet padrão
    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    def create(self, request, *args, **kwargs):
        return Response({'Hello':request.data['nome']})

