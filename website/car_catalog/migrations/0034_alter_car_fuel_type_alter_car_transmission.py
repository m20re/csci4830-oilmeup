# Generated by Django 4.2.11 on 2024-04-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_catalog', '0033_alter_car_fuel_type_alter_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('diesel', 'Diesel'), ('electric', 'Electric'), ('gasoline', 'Gasoline')], default='gasoline', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='automatic', max_length=50),
        ),
    ]
