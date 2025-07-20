from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from sangrah.models import Movie

def index(request):
    return HttpResponse("Welcome to Chitrapat Srushti!")

def movie_list(request):
    movies = Movie.objects.all()
    response = {
        'movies' : list(movies.values())
    }
    # print(list(movies.values()))
    # return JsonResponse(list(movies.values()), safe=False)
    return JsonResponse(response, safe=False)
    
def movie_detail(request, id):
    movie = Movie.objects.filter(id=id)
    if not len(movie):
        return JsonResponse({"movie_detail": ["No Movie Data Found!"]},safe=False)
    response = {
        "movie_detail": movie.values()[0] #list(movie.values()[0])
    }
    return JsonResponse(response, safe=False)