from audioop import reverse
from django.db import models
from django.urls import reverse

# Create your models here.
class Trail (models.Model):
    name = models.CharField(max_length=100)
    terrian = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    length= models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url (self):
       return reverse ('detail', kwargs={'trail_id': self.id})
