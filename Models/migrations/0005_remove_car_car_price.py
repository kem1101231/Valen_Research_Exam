# Generated by Django 2.0 on 2020-03-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0004_auto_20200309_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_price',
        ),
    ]
