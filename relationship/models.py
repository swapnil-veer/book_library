from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.BigIntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    updation_date= models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"

class Aadhar(models.Model):
    aadhar_number = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=250)
    DOB = models.DateField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)    
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    creation_date = models.DateTimeField(auto_now=True)
    updation_date= models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.aadhar_number

    class Meta:
        db_table = "aadhar"

class Fueltype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "fueltype"

class CModel(models.Model):
    name = models.CharField(max_length= 50)
    fueltype = models.ManyToManyField(Fueltype)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "cmodel"

# created by
# updated by
# updated date
# is_active
# 



class Car(models.Model):
    name = models.CharField(max_length=255, unique= True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car"

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "car_model"