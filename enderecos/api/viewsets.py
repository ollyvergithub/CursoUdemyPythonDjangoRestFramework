# Django Rest Framework
# ViewSets define the view behavior.
"""
A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
"""

from rest_framework.viewsets import ModelViewSet
from core.models import Endereco
from .serializers import EnderecosSerializer

class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
