from django.shortcuts import render
# from django.template import loader
from .models import Music

 
# Create your views here.

def homepage(request):
    music=list(Music.objects.all())
    return render(request,'home.html',{
        'music':music
    })



