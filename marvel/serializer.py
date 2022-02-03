from rest_framework import serializers
from marvel.models import Comic, Serie


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ['id', 'title', 'description', 'modified', 'pageCount']
        # fields = '__all__'


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'title', 'description', 'modified', 'startYear', 'endYear']
