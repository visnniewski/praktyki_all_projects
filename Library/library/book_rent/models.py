from django.db import models
from django.contrib.auth.models import User

class author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="no name", max_length=50)
    description = models.CharField(default="no desc", max_length=1000)
    #ok

class book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default="no title", max_length=200)
    author_id = models.ForeignKey(author, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_rented = models.BooleanField(default=False)