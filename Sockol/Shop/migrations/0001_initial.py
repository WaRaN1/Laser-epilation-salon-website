# Generated by Django 4.1.5 on 2023-02-04 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Salon1', '0011_laser_epilation_category_laser_epilation_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('base64', models.TextField(blank=True)),
                ('category_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.category')),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Salon1.icon')),
            ],
        ),
    ]