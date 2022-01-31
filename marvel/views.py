from rest_framework import viewsets
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

        serie_data = request.data
        new_serie = Serie.objects.create(title=serie_data["title"], description=serie_data["description"])
        new_serie.save()
        serializer = SerieSerializer(new_serie)
        return Response(serializer.data)

