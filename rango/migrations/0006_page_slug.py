# Generated by Django 2.2.17 on 2021-01-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20210128_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
