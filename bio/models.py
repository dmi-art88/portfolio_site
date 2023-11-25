from django.db import models


class Bio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
