# Generated by Django 4.1.5 on 2023-02-02 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Salon1', '0008_laser_epilation_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laser_epilation',
            name='type',
        ),
    ]
