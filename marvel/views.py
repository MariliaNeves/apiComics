from django.http import HttpResponse
from rest_framework import viewsets
from marvel.models import Comic
from marvel.serializer import ComicSerializer


class ComicViewSet(viewsets.ModelViewSet):
    """Exibindo Comics"""
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


def teste(request):
    return HttpResponse('<h1>Teste!</h1>')
