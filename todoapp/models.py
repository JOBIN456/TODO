from django.db import models

# Create your models here.
class duty(models.Model):
    name=models.CharField(max_length=250)
    priorty=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
