from django.db import models

# Create your models here.

class Image(models. Model):
    photos = models.ImageField(upload_to="imagedase")
    Date = models.DateTimeField(auto_now_add=True)
