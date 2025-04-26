from django.db import models


class Quotation(models.Model):
    image = models.ImageField(upload_to='uploads/')
    text = models.TextField()
    human = models.CharField(max_length=255)
