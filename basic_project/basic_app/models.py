from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
