from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    lessons = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return self.name
