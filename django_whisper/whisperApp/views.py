from django.shortcuts import render, redirect

from .forms import VideoForm
from .models import Video
import whisper
import os

# Home view
def home(request):
    return render(request, 'home.html')

# Video view
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_in_text')
    else:
        form = VideoForm()

    return render(request, 'upload_video.html', {'form': form})

# Conversión view
def convert_to_text(request):
    model = whisper.load_model("base")
    video = Video.objects.get(pk=1)
    result = model.transcribe(os.getcwd()+video.video_file.url)
    print(result["text"])

    contexto = {'transcripcion':result["text"]}
    return render(request, 'video_in_text.html', contexto)

