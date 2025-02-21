from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    
    GENDER_CHOICES = (
        ('male','Male'),
        ('female', 'Female')
    )
    
    ROLES = (
        ('patient','Patient'),
        ('provider', 'Provider'),
    )
    
    username = models.CharField(max_length=50, unique=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    role = models.CharField(max_length=50, choices=ROLES)
    
    group = models.ManyToManyField(Group, related_name='customuser_group_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permission_set', blank=True)
    
    def __str__(self):
        return self.username
    
class Provider(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50)
    provider_dob = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.f_name}{self.user.l_name}'
    
class Patient(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.f_name}{self.user.l_name}'