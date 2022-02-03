from rest_framework import viewsets, status
from marvel.models import Comic, Serie
from marvel.serializer import ComicSerializer, SerieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ComicViewSet(viewsets.ModelViewSet):
    """Exibindo Comics"""
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


class SerieViewSet(APIView):
    serializer_class = SerieSerializer

    def get_queryset(self):
        series = Serie.objects.all()
        return series

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                series = Serie.objects.get(id=id)
                serializer = SerieSerializer(series)
        except:
            series = self.get_queryset()
            serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        new_serie = Serie.objects.create(title=data["title"], description=data["description"], startYear=data["startYear"], endYear=data["endYear"])
        new_serie.save()
        serializer = SerieSerializer(new_serie)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            data = request.data
            id = data["id"]
            serie_object = Serie.objects.get(id=id)

            serie_object.title = data["title"]
            serie_object.description = data["description"]
            serie_object.startYear = data["startYear"]
            serie_object.endYear = data["endYear"]

            serie_object.save()
            serializer = SerieSerializer(serie_object)
            return Response(serializer.data)
        except:
            return Response('Não encontrado!', status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            serie_object = Serie.objects.get(id=id)
            serie_object.delete()
            return Response('Removido com sucesso!')
        except:
            return Response('Erro ao remover', status=status.HTTP_404_NOT_FOUND)
