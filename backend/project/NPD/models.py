from django.db import models


class File(models.Model):
    description = models.CharField("description/name", max_length=511)
    file = models.FileField(upload_to="media/behavior/")

    def __str__(self):
        return self.description