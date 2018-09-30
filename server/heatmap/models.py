from django.db import models

# Create your models here.
class Video(models.Model):
    file = models.FileField(upload_to = 'uploads/', null = True, verbose_name = "")

    def __str__(self):
        return str(self.file)
