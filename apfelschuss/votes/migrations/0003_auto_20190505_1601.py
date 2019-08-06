# Generated by Django 2.0.13 on 2019-05-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20190504_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='slug_de',
            field=models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='slug_fr',
            field=models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='slug_it',
            field=models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='slug_rm',
            field=models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Voting URL slug'),
        ),
    ]