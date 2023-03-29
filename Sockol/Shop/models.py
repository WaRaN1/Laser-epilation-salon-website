from django.core.validators import MinValueValidator
from django.db import models
from Salon1.models import *
import base64

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Volume1(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Volume2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Shop(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    ref1 = models.IntegerField(validators=[MinValueValidator(1)])
    volume1 = models.ForeignKey(Volume1, on_delete=models.SET_NULL, null=True)
    ref2 = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    volume2 = models.ForeignKey(Volume2, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    category_product = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}, {self.brand}, {self.ref1}-{self.volume1}, {self.ref2}-{self.volume2}"

    class Meta:
        ordering = ['name', 'english_name']



