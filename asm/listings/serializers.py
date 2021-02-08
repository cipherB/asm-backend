from rest_framework import serializers
from .models import Anime, Series, Movies

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('pk', 'title', 'slug', 'types', 'genre', 'rank', 'year_released', 'image', 'ratings', 'rated', 'description',)

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('pk', 'title', 'slug', 'types', 'genre', 'rank', 'year_released', 'image', 'ratings', 'rated', 'description',)

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('pk', 'title', 'slug', 'types', 'genre', 'rank', 'year_released', 'image', 'ratings', 'rated', 'description',)
