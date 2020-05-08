from django.db import models


class Course(models.Model):
    course_id = models.CharField(max_length=200, unique=True)

    subject   = models.CharField(max_length=200)
    number    = models.CharField(max_length=200)
    title     = models.CharField(max_length=200)

    def __str__(self):
        return self.subject + " " + self.number
    

class Section(models.Model):
    class_number = models.CharField(max_length=200, unique=True)

    course       = models.ForeignKey(Course, on_delete=models.CASCADE)

    name         = models.CharField(max_length=200)  # L01
    status       = models.CharField(max_length=200)  # open closed cancelled
    start_time   = models.CharField(max_length=200)
    end_time     = models.CharField(max_length=200)
    days         = models.CharField(max_length=200)  # M W F

    def __str__(self):
        return str(self.course) + " " + self.name


class Subscription(models.Model):
    section   = models.ForeignKey(Section, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)
    email     = models.EmailField(max_length=200)
    phone     = models.CharField(max_length=200, blank=True)
    isActive  = models.BooleanField(default=True)

    def __str__(self):
        return str(self.section) + " -> " + self.email
