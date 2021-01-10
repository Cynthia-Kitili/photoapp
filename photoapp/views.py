from django.shortcuts import HttpResponse

def welcome(request):
    return HttpResponse('Welcome to the Photoapp')

# Create your views here.
