# Generated by Django 2.2.7 on 2021-12-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_car_thumbnail_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='decription',
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=''),
        ),
    ]