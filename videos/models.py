from django.db import models


class HTMLVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, unique=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created_at',)

class TailwindVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, unique=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created_at',)


class PythonVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, unique=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created_at',)


class DjangoVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, unique=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created_at',)