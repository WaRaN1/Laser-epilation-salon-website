# Generated by Django 4.1.5 on 2023-03-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salon1', '0012_type_service_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='type_service',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
