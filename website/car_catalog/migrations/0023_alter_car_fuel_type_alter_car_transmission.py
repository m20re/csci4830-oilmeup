# Generated by Django 4.2.11 on 2024-04-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_catalog', '0022_alter_car_fuel_type_alter_car_transmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('gasoline', 'Gasoline'), ('electric', 'Electric'), ('diesel', 'Diesel')], default='gasoline', max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='automatic', max_length=50),
        ),
    ]
