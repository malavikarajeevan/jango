from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=250)
    priority=models.IntegerField()
    
    def _str_(self):
        return self.task
