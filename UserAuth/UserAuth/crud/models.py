from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="title")
    body = models.CharField(max_length=1200, default="body")
    date = models.DateField(default=timezone.now().date())
    user_id = models.IntegerField(default=1)