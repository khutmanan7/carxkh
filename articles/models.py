from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    thumb0 = models.ImageField(blank=True)

    subHeading1 = models.CharField(max_length=100, blank=True)
    text1 = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    subHeading2 = models.CharField(max_length=100, blank=True)
    text2 = models.TextField(blank=True)
    image2 = models.ImageField(blank=True)
    subHeading3 = models.CharField(max_length=100, blank=True)
    text3 = models.TextField(blank=True)
    image3 = models.ImageField(blank=True)
    subHeading4 = models.CharField(max_length=100, blank=True)
    text4 = models.TextField(blank=True)
    image4 = models.ImageField(blank=True)
    subHeading5 = models.CharField(max_length=100, blank=True)
    text5 = models.TextField(blank=True)
    image5 = models.ImageField(blank=True)
    subHeading6 = models.CharField(max_length=100, blank=True)
    text6 = models.TextField(blank=True)
    image6 = models.ImageField(blank=True)
    subHeading7 = models.CharField(max_length=100, blank=True)
    text7 = models.TextField(blank=True)
    image7 = models.ImageField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=25, default='carr')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text1[:50] + '...'
