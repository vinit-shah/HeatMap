from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.
def home(request):
	image_src = static('leafs.jpeg') # Load in heatmap
	html = "<html><body><image src='%s'></body></html>" % image_src
	return HttpResponse(html)