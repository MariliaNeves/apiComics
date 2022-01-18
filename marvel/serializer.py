from rest_framework import serializers
from marvel.models import Comic


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ['title', 'description', 'modified', 'pageCount']
        # fields = '__all__'
