# Generated by Django 2.0.13 on 2019-05-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_auto_20190513_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='admin_pro',
            new_name='official_pro',
        ),
    ]