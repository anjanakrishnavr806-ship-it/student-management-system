from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'students'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        app_label = 'students'

    def __str__(self):
        return self.name

  
