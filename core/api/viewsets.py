# Django Rest Framework
# ViewSets define the view behavior.
"""
A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
"""
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    # Com a chamada do método get_queryset
    #queryset = PontoTuristico.objects.filter(aprovado=True)
    # Sobescrevendo o método get_queryset. Aqui filtramos e retornamos um iterable
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    serializer_class = PontoTuristicoSerializer