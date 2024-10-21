from django.db import models


class data(models.Model):
    NAME = models.CharField(max_length=255)
    Stock = models.CharField(max_length=255)
    Price = models.FloatField()
    image = models.ImageField(upload_to='', max_length=2000, null=True, blank=True)

    def __str__(self):
        return f"{self.NAME} - ${self.Stock}"

class offer(models.Model):
    code = models.CharField(max_length=255)
    discount = models.FloatField()

