from django.shortcuts import render, redirect

from django_whisper.django_whisper.settings import BASE_DIR
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
            return redirect('home')  # Reemplaza 'nombre_de_tu_vista' con la vista a la que quieres redirigir después de cargar el video.
    else:
        form = VideoForm()

    return render(request, 'upload_video.html', {'form': form})

# Conversión view
def convert_to_text(request):
    model = whisper.load_model("base")
    video = Video.objects.get(pk=1)
    video_url = video.video_file.url
    print(video_url)
    print(os.getcwd())
    #result = model.transcribe(video_url)
    result = model.transcribe("/media/videos/audio_prueba.mp3")
    print(result["text"])

    contexto = {'transcripcion':result["text"]}
    return render(request, 'video_in_text.html', contexto)

