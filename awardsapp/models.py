from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
# from __future__ import unicode_literals
import numpy as np
from django.db.models.signals import post_save
from django.db.models import Avg, Max, Min

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = CloudinaryField('image')
    description = models.TextField()
    project_url=models.URLField(max_length=250)

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

    def save_project(self):
        self.save()

    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def update_project(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    @classmethod
    def update_description(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    image=models.ImageField(upload_to='picture/', )
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    description=models.TextField()
    location=models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    tags=models.ManyToManyField(tags, blank=True)
    likes = models.IntegerField(default=0)
    comments= models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures

    @classmethod
    def filter_by_tag(cls, tags):
        pictures = cls.objects.filter(tags=tags)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location=location)
        return pictures

    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures

    @classmethod
    def update_description(cls, id):
        pictures = cls.objects.filter(id=id).update(id=id)
        return pictures

