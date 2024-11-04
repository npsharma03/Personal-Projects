
from django.db import models


from django.db import models
from django.contrib.auth.models import User

#class User(models.Model):
    #username = models.CharField(max_length = 256, unique=True, default = 'sharmanik', null=False)
    #email = models.EmailField(max_length=256, null=True)
    #name = models.CharField(max_length=256, null=True)
    #role = models.CharField(max_length=10, null=True)
    #password = models.CharField(max_length=256,null=True)

class Course(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    number = models.CharField(max_length=5)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Rosters(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    lecture_id = models.AutoField(primary_key=True)

class QRCode(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(null=True)
    code = models.CharField(max_length=255, unique=True, primary_key=True)

