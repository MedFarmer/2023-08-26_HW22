from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.image.url

class Student(models.Model):
    name = models.CharField(max_length=30)
    grade = models.FloatField()
    
    def __str__(self):
        return self.name

# Create your models here.
