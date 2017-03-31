from django.db import models

# Create your models here.
class Part(models.Model):
    part_id = models.CharField(max_length=64)
    description = models.CharField(max_length=128, default='', blank=True)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.part_id
