# Generated by Django 4.2.2 on 2023-06-29 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0004_alter_car_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='car',
            table='car',
        ),
        migrations.AlterModelTable(
            name='carmodel',
            table='car_model',
        ),
    ]
