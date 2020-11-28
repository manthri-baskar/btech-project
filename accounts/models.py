from django.db import models

# Create your models here.

class register(models.Model):
    First_name = models.CharField(max_length= 150, null=True, db_index=True)
    Last_name = models.CharField(max_length= 150,  null=True, db_index=True)
    username = models.CharField(max_length= 150,  null=True, db_index=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length= 150, null=True,  db_index=True)
    confirm_password = models.CharField(max_length= 150,  null=True, db_index=True)

