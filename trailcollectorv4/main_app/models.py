from audioop import reverse
from django.db import models
from django.urls import reverse

TASKS = (
    ('B', 'Blaze repairt'),
    ('C', 'Cut branches'),
    ('G','Garbage collecting')
)

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


class Maintaining(models.Model):
    date = models.DateField("Maintaining Time")
    task = models.CharField(
      max_length=1,
      choices=TASKS,
      default=TASKS[0][0]
  )
    
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)
    def __str__(self):
      return f"{self.get_task_display()} on {self.date}"