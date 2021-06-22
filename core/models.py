from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.author


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    comments = GenericRelation(Comment)
    
    def __str__(self):
        return self.title

    
class Profile(models.Model):
    about = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comments = GenericRelation(Comment)

    def __str__(self):
        return f'profile of {self.user.username}'

