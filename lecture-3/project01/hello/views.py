from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "hello/index.html")

def pradeep(request):
  return HttpResponse("Hello, Pradeep!")

def mani(request):
  return HttpResponse("Hello, Mani!")

def greet(request, name):
  return render(request, "hello/greet.html", {"name": name.capitalize()})
