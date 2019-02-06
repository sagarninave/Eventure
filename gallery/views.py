from django.http import HttpResponse 
from django.shortcuts import render
from .models import gallery

def index(request):
	all_images = gallery.objects.all().order_by('-id')
	context = {'all_images' : all_images}
	return render(request, 'gallery/index.html', context)

