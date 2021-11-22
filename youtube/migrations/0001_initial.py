# Generated by Django 3.0.8 on 2020-07-17 07:24

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import youtube.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('tags', models.CharField(max_length=500, null=True)),
                ('video', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comm', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.Video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='Youtube_VideoList')),
                ('source_files', models.FileField(blank=True, null=True, upload_to=youtube.models.VideoListSourceFilePath)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSubComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comm', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.VideoComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.Video')),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='video_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='youtube.VideoList'),
        ),
    ]
