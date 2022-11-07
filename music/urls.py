from django.urls import path
from .views import homepage

app_name='music'

urlpatterns= [

   path('',homepage,name='home_page'),

]