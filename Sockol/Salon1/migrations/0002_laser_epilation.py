# Generated by Django 4.1.5 on 2023-02-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salon1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laser_epilation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
