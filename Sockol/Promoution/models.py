from django.db import models
from Salon1.models import *

class Promoution(models.Model):
    date = models.DateTimeField(auto_now=False, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(Type_service, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category_service, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.date}, {self.type}, {self.category}, {self.size}"

