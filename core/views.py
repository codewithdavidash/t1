from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm
from videos.models import *

@login_required
def index(request):
    html = HTMLVideo.objects.all()
    tailwindcss = TailwindVideo.objects.all()
    python = PythonVideo.objects.all()
    django = DjangoVideo.objects.all()
    return render(request, 'core/index.html', {
        'html': html,
        'tailwindcss': tailwindcss,
        'python': python,
        'django': django
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
        return render(request, 'core/signup.html', {
            'form': form
        })
