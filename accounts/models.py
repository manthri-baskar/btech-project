from django.db import models

# Create your models here.

class register(models.Model):
    First_name = models.CharField(max_length= 150,blank=True)
    Last_name = models.CharField(max_length= 150,blank=True)
    Username = models.CharField(max_length= 150,unique=True)
    Email_ID = models.EmailField(unique=True)
    Password = models.CharField(max_length= 150)
    Confirm_password = models.CharField(max_length= 150)

    def __str__(self):
        return self.Username

