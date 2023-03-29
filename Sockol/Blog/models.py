from django.db import models
from Salon1.models import *

class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']
