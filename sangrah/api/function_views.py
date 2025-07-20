from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from sangrah.models import Movie
from .serializers import MovieSerializer

def index(request):
    return HttpResponse("Welcome to Chitrapat Srushti!")

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method =="GET": 
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    if request.method =="POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    if request.method =="GET":    
        movie = Movie.objects.filter(id=id)
        if not len(movie):    
            return Response({"error" : f"Movie with id:{id} not found"},status=status.HTTP_400_BAD_REQUEST)
        else: 
            serializer = MovieSerializer(movie, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method =="PUT":
        movie = Movie.objects.filter(id=id)
        serializer = MovieSerializer(movie[0], data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =="DELETE":
        movie = Movie.objects.filter(id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)