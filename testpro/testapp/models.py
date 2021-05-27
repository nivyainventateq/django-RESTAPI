from django.db import models

# Create your models here.
class ordertb(models.Model):
    oid=models.IntegerField()
    item=models.CharField(max_length=256)
    price=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item