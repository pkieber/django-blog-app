from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateTimeField(auto_now_add=True) # add date automatically
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete article if user is deleted
    featured = models.BooleanField(default=False) # featured article
    likes = models.ManyToManyField(User, related_name="likes", blank=True) # like article
