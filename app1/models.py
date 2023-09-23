from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-date"]

       

   
    