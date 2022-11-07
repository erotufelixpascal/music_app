from django.conf.urls import path
from .views import homepage

app_name='musics'

urlpatterns= [

   path('',homepage,name='home'),

]