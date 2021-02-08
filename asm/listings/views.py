from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Anime, Series, Movies
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def anime_list(request):
    if request.method == 'GET':
        data = Anime.objects.all()
        serializer = AnimeSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['Get'])
def anime_detail(request, slug):
    if request.method == 'GET':
        print(slug)
        data = Anime.objects.filter(slug=slug)
        serializer = AnimeSerializer(data, context={'request': request}, many=True )
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def series_list(request):
    if request.method == 'GET':
        data = Series.objects.all()
        serializer = SeriesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(SeriesSerializer(data=request.data))
        serializer = SeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['Get'])
def series_detail(request, slug):
    if request.method == 'GET':
        data = Series.objects.filter(slug=slug)
        serializer = SeriesSerializer(data, context={'request': request}, many=True )
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        data = Movies.objects.all()
        serializer = MoviesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['Get'])
def movies_detail(request, slug):
    if request.method == 'GET':
        data = Movies.objects.filter(slug=slug)
        serializer = MoviesSerializer(data, context={'request': request}, many=True )
        return Response(serializer.data)

