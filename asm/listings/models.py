from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Anime(models.Model):
    title = models.CharField(("title"), max_length=50)
    slug = models.SlugField(max_length=150, blank=True)
    types = models.CharField(("type"), max_length=50)
    genre = models.CharField(("genre"), max_length=50)
    rank = models.IntegerField()
    year_released = models.CharField(("year"), max_length=50)
    image = models.ImageField(upload_to='photos/anime/')
    ratings = models.FloatField()
    rated = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Series(models.Model):
    title = models.CharField(("title"), max_length=50)
    slug = models.SlugField(max_length=150, blank=True)
    types = models.CharField(("type"), max_length=50)
    genre = models.CharField(("genre"), max_length=50)
    rank = models.IntegerField()
    year_released = models.CharField(("year"), max_length=50)
    image = models.ImageField(upload_to='photos/series/')
    ratings = models.FloatField()
    rated = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Movies(models.Model):
    title = models.CharField(("title"), max_length=50)
    slug = models.SlugField(max_length=150, blank=True)
    types = models.CharField(("type"), max_length=50)
    genre = models.CharField(("genre"), max_length=50)
    rank = models.IntegerField()
    year_released = models.CharField(("year"), max_length=50)
    image = models.ImageField(upload_to='photos/movies/')
    ratings = models.FloatField()
    rated = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)



