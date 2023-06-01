from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

