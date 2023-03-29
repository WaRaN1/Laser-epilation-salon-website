# Generated by Django 4.1.5 on 2023-02-05 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_remove_shop_volume2_alter_shop_volume1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volume2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Volume',
            new_name='Volume1',
        ),
        migrations.AddField(
            model_name='shop',
            name='volume2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.volume2'),
        ),
    ]
