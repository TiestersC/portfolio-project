from django.db import models

# Create your models here.

# Create a Blog Models
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images')

# Google django model fields to find the different possibilities