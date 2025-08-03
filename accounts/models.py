from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# create customuser and inherit from abstractuser
class CustomUser(AbstractUser):
    ROLES_CHOICES = [
        ('admin', 'ADMIN'),
        ('sales', 'SALES')
    ]
    role = models.CharField(max_length=100, choices=ROLES_CHOICES, default='sales')


class Student(models.Model):
    added_by = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    skillset = models.CharField(max_length=200)
    state = models.CharField(max_length=100)


def __str__(self):
    return self.name
