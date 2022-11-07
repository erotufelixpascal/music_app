from django.shortcuts import render
# from django.template import loader
from .models import Music

 
# Create your views here.

def homepage(request):
    music=Music.object.all()
    return render(request,'home.html')



