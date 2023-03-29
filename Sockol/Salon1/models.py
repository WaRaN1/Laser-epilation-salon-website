from django.db import models
import base64


class Icon(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="Product_shop/static/icons")
    base64 = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.base64 = base64.b64encode(self.icon.read()).decode('utf-8')
        super(Icon, self).save(*args, **kwargs)


class Category_service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Type_service(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"


class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Laser_epilation(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category_service, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type_service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.type}, {self.name}, {self.gender}, {self.price}"

