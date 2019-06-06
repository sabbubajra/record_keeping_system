from django.db import models
from datetime import date
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your models here.
GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)

SEMESTER_CHOICES=(
    ('Select','Select'),
    ('First','First'),
    ('Second','Second'),
    ('Third','Third'),
    ('Fourth','Fourth'),
    ('Fifth','Fifth'),
    ('Sixth','Sixth'),
    ('Seventh','Seventh'),
    ('Eighth','Eighth')
)
class Addstudent(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    image=models.FileField(upload_to='detailabtstudent',blank=True)
    date_of_birth=models.DateField()
    admission_date=models.DateField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=10,default='S')
    semester=models.CharField(choices=SEMESTER_CHOICES,max_length=20)
    mobileno=models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detailabtstudent:studentlist',kwargs={'pk':self.pk})

class Addteachers(models.Model):
    name=models.CharField(max_length=50)
    contactno=models.IntegerField()
    email=models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to='Teachers',blank=True)

    def __str__(self):
        return self.name