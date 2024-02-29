from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_approved = models.BooleanField(default=False)

class CryptoApi(models.Model):
    slug = models.CharField(max_length=100, null=False, blank=False)
    convert = models.CharField(max_length=100, null=False, blank=False)

class ModelApi(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()