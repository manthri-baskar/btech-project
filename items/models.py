from django.db import models

# Create your models here.

class additem(models.Model):
    Item_name = models.CharField(max_length= 150,blank=True)
    Order_advertisment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    Transportation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    Anti_deteriorate_cost = models.DecimalField(max_digits=10, decimal_places=2)
    Usable_time = models.DecimalField(max_digits=10, decimal_places=2)
    Lead_time = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Item_name

