from django.db import models
from django.utils import timezone


class News(models.Model):
    Header = models.CharField(verbose_name="Header", max_length=511)
    description = models.CharField(max_length=511)
    img = models.ImageField(upload_to="media/")
    date = models.CharField(verbose_name="Date", max_length=4047, default=timezone.now)
    text = models.CharField(max_length=4047)
    ref = models.CharField(max_length=5011)

    def __str__(self):
        return self.Header


class NewsOld(models.Model):
    Header = models.CharField(verbose_name="Header", max_length=511)
    description = models.CharField(max_length=511)
    img = models.ImageField(upload_to="media/")
    date = models.CharField(verbose_name="Date", max_length=4047, default=timezone.now)
    text = models.CharField(max_length=4047)
    ref = models.CharField(max_length=5011)

    def __str__(self):
        return self.Header