from cProfile import label
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = '__all__'
        #widgets = {'video_file' : forms.FileInput(attrs={'class' : 'custom-file-input','placeholder': 'Any file selected'})}
        #label = 'Select file'
    
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['video_file'].widget = forms.ClearableFileInput(
            attrs={'placeholder': 'Any file selected'},
        )
        self.fields['video_file'].label = 'Select file'