# Generated by Django 3.1.3 on 2020-11-25 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additem',
            old_name='advertise',
            new_name='advertising_cost',
        ),
        migrations.RenameField(
            model_name='additem',
            old_name='anti_deteriorat',
            new_name='anti_deterioration_cost',
        ),
        migrations.RenameField(
            model_name='additem',
            old_name='name',
            new_name='item_name',
        ),
        migrations.RenameField(
            model_name='additem',
            old_name='transport',
            new_name='transportation_cost',
        ),
        migrations.RenameField(
            model_name='additem',
            old_name='time_period',
            new_name='usable_timeperiod',
        ),
    ]
