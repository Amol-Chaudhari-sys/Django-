from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class student(models.Model):
    # id = models.AutoField()      # utomaticaly add by Django no need to defien 
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField()

class Car(models.Model):
    car_name= models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self)->str:
        return self.car_name
    
@receiver(post_save, sender=Car)
def call_car_api(sender, instance,  **kwargs):
    print ("car object Created" )
    print (sender , instance , kwargs)
    
