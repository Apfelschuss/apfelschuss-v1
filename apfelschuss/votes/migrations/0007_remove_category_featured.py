# Generated by Django 2.0.13 on 2019-05-21 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_auto_20190516_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='featured',
        ),
    ]