from django.db import models

class MovieInfo(models.Model):
    title = models.CharField(max_length=25)
    year = models.IntegerField(max_length=4)
    summary = models.TextField(max_length=50)
    def __str__(self):
        return self.title
