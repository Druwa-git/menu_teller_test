from django.db import models

class Record(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    file_url = models.URLField(max_length=200, blank=True, null=True, default='')
    # file = models.FileField(upload_to='tts/', blank=True, null=True, default='')

class Menu(models.Model):
    title = models.CharField(max_length=100)
    file_url = models.URLField(max_length=200, blank=True, null=True, default='')
# Create your models here.