from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h1 align=center> Hello User </br> Please go to <strong> https://127.0.0.1:8000/home </strong>  for home page </h1>")
