from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from videos.models import *

@login_required
def add_videos(request):
    return render(request, 'videos/add.html', {})

@login_required
def html(request):
    if request.method == 'POST':
        form = HtmlVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = HtmlVideoForm()
    return render(request, 'videos/html.html', {
            'form': form
    })

@login_required
def python(request):
    if request.method == 'POST':
        form = PythonVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PythonVideoForm()
    return render(request, 'videos/python.html', {
            'form': form
    })

@login_required
def tailwind(request):
    if request.method == 'POST':
        form = TailwindVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TailwindVideoForm()
    return render(request, 'videos/tailwind.html', {
            'form': form
    })

@login_required
def django(request):
    if request.method == 'POST':
        form = DjangoVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DjangoVideoForm()
        return render(request, 'videos/django.html', {
            'form': form
        })

@login_required
def detail(request, pk):
    html = get_object_or_404(HTMLVideo, pk=pk)
    return render(request, 'videos/detail.html', {
        'html': html
    })