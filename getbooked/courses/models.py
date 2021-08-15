from django.db import models

# Create your models here.
class Course(models.Model):
    verbose_name_plural = 'Courses'
    name = models.TextField()
    description = models.TextField()
    day = models.TextField()
    time = models.TextField()
    places = models.TextField()