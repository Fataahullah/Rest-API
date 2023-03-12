from django.db import models

# Create your models here.
#Creating user model

class User(models.Model):
    first_name=models.CharField(max_length=30,)    
    last_name=models.CharField(max_length=30,)
    email=models.EmailField(unique=True)
    mobile_no=models.CharField(unique=True,max_length=13)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Customer(models.Model):
    profile_number=models.CharField(max_length=25)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    