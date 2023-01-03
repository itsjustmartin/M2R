from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def mainpage(request):
    return HttpResponse("this is the main page")
