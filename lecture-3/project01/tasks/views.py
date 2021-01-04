from django import forms
from django.shortcuts import render
from django.middleware import csrf

class NewForm(forms.Form):
  task = forms.CharField(label="New Task")
  priorities = forms.IntegerField(label="priorities")

tasks = ["read", "write", "copy", "paste"]
# Create your views here.
def index(request):
  return render(request, "tasks/index.html", {"tasks":tasks})

def add(request):
  return render(request, "tasks/add.html", {"form":NewForm()})
