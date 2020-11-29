from django.db import models





# Create your models here.
class additem(models.Model):
    item_name = models.CharField(max_length= 150, unique=True, db_index=True)
    advertising_cost = models.DecimalField(max_digits=10, decimal_places=2)
    transportation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    anti_deterioration_cost = models.DecimalField(max_digits=10, decimal_places=2)
    usable_timeperiod = models.IntegerField()
    lead_time = models.IntegerField()

    def __str__(self):
      return self.item_name