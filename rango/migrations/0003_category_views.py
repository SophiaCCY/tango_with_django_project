# Generated by Django 2.2.17 on 2021-01-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210125_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
