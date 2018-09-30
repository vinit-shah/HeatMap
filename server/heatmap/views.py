from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import Video
from .forms import VideoForm

# Create your views here.
def home(request):
	file = None
	heatmap = None

	form = VideoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		video = form.save()
		file = video.file
		# Gen data from video
		heatmap = static("leafs.jpeg") # Gen heatmap
		video.delete() # Unless we want to save this

	context= {
	          'file': file,
              'form': form,
              'heatmap': heatmap
              }
    
	return render(request, 'upload.html', context)