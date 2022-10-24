from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def playgame(request):
    return (HttpResponse('Game is running'))
