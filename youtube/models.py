from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

def VideoListSourceFilePath(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'youtube/videos/source_files/{0}/{1}'.format(instance.title, filename) 

class VideoList(models.Model):
	title = models.CharField(max_length=50, unique=True)
	description = models.CharField(max_length=150)
	image = models.ImageField(upload_to='youtube/VideoList')
	source_files = models.FileField(upload_to = VideoListSourceFilePath, null=True, blank=True) 

	def __str__(self):
		return f'{self.title}'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Video(models.Model):
	title = models.CharField(max_length=100)
	desc = RichTextUploadingField(null=True)
	tags = models.CharField(max_length=500, null=True)
	video = models.CharField(max_length=20)
	video_list = models.ForeignKey(VideoList, on_delete=models.SET_NULL, null=True)

class VideoComment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()

class VideoSubComment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	comment = models.ForeignKey(VideoComment, on_delete=models.CASCADE)