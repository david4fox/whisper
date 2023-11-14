from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path('upload/', views.upload_video, name='upload_video'),
    path('text/', views.convert_to_text, name='video_in_text'),
]