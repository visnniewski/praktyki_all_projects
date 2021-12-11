from django.db import models

class Albums(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200, default='0000000')
    album_id = models.ForeignKey(Albums, on_delete=models.CASCADE)

    def __str__(self):
        return self.title