from rest_framework import serializers
from . import models


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'student_name', 'student_address','student_file')
#         model = models.Student

from rest_framework import serializers
from .models import Student1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','address')
        model = models.Student1

