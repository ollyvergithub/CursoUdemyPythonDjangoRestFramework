"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Django Rest Framework
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# Com a chamada do método get_queryset - Necessário atribuir o base_name com o nome do Model.
#router.register(r'pontoturistico',PontoTuristicoViewSet)
router.register(r'pontoturistico',PontoTuristicoViewSet, base_name='PontoTuristico')

router.register(r'atracoes',AtracaoViewSet)
router.register(r'enderecos',EnderecosViewSet)
router.register(r'comentarios',ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django Rest Framework
    path('', include(router.urls))
]
