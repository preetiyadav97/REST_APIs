from django.db import models


# Create your models he
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll=models.IntegerField()
    city=models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
