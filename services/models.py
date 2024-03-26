from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
      video = EmbedVideoField()
      discription = models.TextField(default='')


class Project(models.Model):
      title = models.CharField(max_length=100)
      description = models.TextField()
      url = models.URLField()
      
class Article(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)      