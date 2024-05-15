from django.db import models

# Create your models here.

class loan(models.Model):
    name = models.CharField(max_length=60)
    amount = models.IntegerField()

    def __str__(self):
        return self.name