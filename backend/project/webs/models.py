from django.db import models


class Webinar(models.Model):
    header = models.CharField("description/name", max_length=511)
    img = models.ImageField(upload_to="media/webinars")
    ref = models.CharField("main page ref", max_length=255)
    type = models.CharField("Вебинар, Совещание...", max_length=255)

