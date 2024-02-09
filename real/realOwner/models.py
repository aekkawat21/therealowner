from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True,blank=True)
    model = models.CharField(max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    serial_number = models.CharField(max_length=255, unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.serial_number}"
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100 , blank=True, null=True)
    age = models.PositiveIntegerField(max_length=100 , blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'ชาย'),
        ('F', 'หญิง'),
        ('O', 'อื่น'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    phone_number = models.CharField(max_length=15,blank=True, null=True)

    def __str__(self):
        return self.name
       

