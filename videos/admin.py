from django.contrib import admin
from .models import HTMLVideo, TailwindVideo, PythonVideo, DjangoVideo

admin.site.register([HTMLVideo, TailwindVideo, PythonVideo, DjangoVideo])