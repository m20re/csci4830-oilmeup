# Generated by Django 4.2.11 on 2024-04-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('electric', 'Electric'), ('gasoline', 'Gasoline'), ('diesel', 'Diesel')], default='gasoline', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars_images'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='automatic', max_length=50),
        ),
    ]
