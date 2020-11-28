# Generated by Django 3.1.3 on 2020-11-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('advertise', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transport', models.DecimalField(decimal_places=2, max_digits=10)),
                ('anti_deteriorat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_period', models.IntegerField()),
                ('lead_time', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='mohan1',
        ),
    ]