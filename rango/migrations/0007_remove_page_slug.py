# Generated by Django 2.2.17 on 2021-01-29 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_page_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
