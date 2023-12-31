# Generated by Django 4.2.3 on 2023-07-16 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_djangovideo_video_alter_htmlvideo_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangovideo',
            name='description',
            field=models.TextField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='htmlvideo',
            name='description',
            field=models.TextField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pythonvideo',
            name='description',
            field=models.TextField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tailwindvideo',
            name='description',
            field=models.TextField(blank=True, max_length=255, unique=True),
        ),
    ]
