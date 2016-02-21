from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    fileNeeded = models.FileField(blank=True, null=True)
    resolved_by = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def numberOfResolutions(self):
        return self.resolved_by.count()
