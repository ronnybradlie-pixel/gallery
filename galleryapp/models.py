from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    uploader =models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title