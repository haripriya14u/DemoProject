from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length = 50)
    student_address = models.TextField()
    student_file = models.FileField(upload_to = "documents",default='NA')

    def __str__(self):
        return self.student_name

    class Meta:
        verbose_name_plural = 'Student_Details'

class Student1(models.Model):
    name = models.CharField(max_length = 20)
    address = models.TextField()

    def __str__(self):
        return self.name



