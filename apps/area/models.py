from django.db import models


class Pgs(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=510)
    area = models.CharField(max_length=30)
    category = models.CharField(max_length=20, default=False)

    class Meta:
        verbose_name_plural = 'Pgs'

    def __str__(self):
        return self.area
