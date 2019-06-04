# Django Rest Framework
# ViewSets define the view behavior.
"""
A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
"""
from rest_framework.decorators import action
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
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset
        #return PontoTuristico.objects.filter(aprovado=True)

    # Sobescrevendo o método list() do ModelViewSet padrão
    def list(self, request, *args, **kwargs):
        #return Response({'teste': 123})
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        #return Response({'Hello':request.data['nome']})
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # Chamando os métodos padrões no ModelViewSet
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # Criando uma action personalizada para um ponto turistico unico
    @action(detail=True, methods=['get'])
    def denunciar(self, request, pk=None):
        pass

    # Criando uma action personalizada para o endpoint geral - EX: Excluir Todos. Method = DELETE
    @action(detail=False, methods=['get'])
    def teste(self, request, pk=None):
        pass

