# Generated by Django 4.1.5 on 2023-02-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_volume2_rename_volume_volume1_shop_volume2'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='english_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
