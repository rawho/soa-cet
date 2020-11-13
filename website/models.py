from django.db import models
from django.urls import reverse
# Create your models here.



class Artist(models.Model):
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=250, default='a')
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    branch = models.CharField(max_length=250, null=True)
    semester = models.CharField(max_length=250, null=True)
    instagram = models.URLField(default='https://www.instagram.com/<your-user-name>', blank=True)
    facebook = models.URLField(default='https://www.facebook.com/<your-user-name>', blank=True)
    
    dp = models.ImageField(null=True, blank=True, upload_to='dp')
    fav_art = models.ImageField(null=True, blank=True, upload_to='fav_art')



    def __str__(self):
        return self.name

class Image(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    work = models.ImageField(null=True, blank=True, upload_to='works')

    def __str__(self):
        return self.artist.name
