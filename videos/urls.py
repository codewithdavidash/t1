from django.urls import path
from . import views

app_name = 'videos'

urlpatterns = [
    path('add_videos', views.add_videos, name='add'),
    path('add_html_videos/', views.html, name='html'),
    path('add_tailwind_videos/', views.tailwind, name='tailwind'),
    path('add_python_videos/', views.python, name='python'),
    path('add_django_videos/', views.django, name='django'),
    path('<int:pk>/', views.detail, name='detail')
]
