from operator import itemgetter
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os
from django.conf import settings
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100 , blank=True, null=True)
    age = models.PositiveIntegerField(max_length=100 , blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'ชาย'),
        ('F', 'หญิง'),
        ('O', 'อื่น'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)



class Item(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,blank=True, null=True)
    brand = models.CharField(max_length=255,null=True,blank=True)
    model = models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    serial_number = models.CharField(max_length=255, unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True,blank=True)
    store_date_of_purchase = models.DateField(default=timezone.now)
    store_of_purchase = models.CharField(max_length=100,null=True,blank=True)
    warranty = models.TextField(null=True,blank=True)
    previous_owner = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} Item {self.id} - {self.serial_number}"
    