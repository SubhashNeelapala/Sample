from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# from polls.base import BaseModel

ALLOW_NUMBER_ONLY = RegexValidator(r'^[0-9]*$',
                                   'Only numeric characters are allowed.')

class Department(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name_plural = "Department"
        verbose_name = 'Department'
        ordering = ('name',)

class Gender(models.Model):
    name=models.CharField(max_length=6)
    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        verbose_name_plural= "Gender"
        verbose_name="Gender"
        ordering=('name',)

class User(AbstractUser):
    AbstractUser._meta.get_field('first_name').max_length = 60
    AbstractUser._meta.get_field('last_name').max_length = 60
    age = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10,
                                    validators=[ALLOW_NUMBER_ONLY],
                                    unique=True,
                                    db_index=True,
                                    blank=True,
                                    )
    AbstractUser._meta.get_field('email').max_length = 60
    department = models.ForeignKey(Department, blank=True, null=True)
    gender = models.ForeignKey(Gender,blank=True,null=True)
    
    def __str__(self):
        return '%s' % self.username

    class Meta:
        verbose_name_plural = "User" 
        verbose_name = 'User'
        ordering = ('username',)