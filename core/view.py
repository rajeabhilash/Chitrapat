from django.shortcuts import HttpResponse

def index(request):
    response = "<h1 align='center'>Welcome to Chitrapat Srushti! </h1>"
    return HttpResponse(response)