from django import forms
from .models import HTMLVideo, DjangoVideo, TailwindVideo, PythonVideo

INPUT_CLASSES = "w-[15rem] px-3 py-2 text-md rounded-lg"
INPUT_TEXTAREA = "w-[15rem] px-3 py-2 text-md rounded-lg"

class HtmlVideoForm(forms.ModelForm):
    class Meta:
        model = HTMLVideo
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_TEXTAREA
    }))
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))

class DjangoVideoForm(forms.ModelForm):
    class Meta:
        model = DjangoVideo
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_TEXTAREA
    }))
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))    

class TailwindVideoForm(forms.ModelForm):
    class Meta:
        model = TailwindVideo
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_TEXTAREA
    }))
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))    

class PythonVideoForm(forms.ModelForm):
    class Meta:
        model = PythonVideo
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_TEXTAREA
    }))
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    })) 