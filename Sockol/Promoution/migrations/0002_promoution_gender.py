# Generated by Django 4.1.5 on 2023-02-11 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Salon1', '0011_laser_epilation_category_laser_epilation_type'),
        ('Promoution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoution',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Salon1.gender'),
        ),
    ]