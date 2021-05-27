from django.db import models

# Create your models here.

class Contactus(models.Model):
    name1 = models.CharField(max_length=100)
    phoneno =models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name1