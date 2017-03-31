from django.db import models

# Create your models here.
class Part(models.Model):
    part_id = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, default='')
    price = models.FloatField()
    
    def __str__(self):
        return self.part_id
