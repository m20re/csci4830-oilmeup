# Generated by Django 4.2.11 on 2024-04-18 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_catalog', '0014_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('electric', 'Electric'), ('gasoline', 'Gasoline'), ('diesel', 'Diesel')], default='gasoline', max_length=50),
        ),
    ]