# Generated by Django 2.0.13 on 2019-05-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='slug',
        ),
        migrations.AddField(
            model_name='voting',
            name='slug_de',
            field=models.SlugField(blank=True, max_length=80, verbose_name='Voting URL slug'),
        ),
        migrations.AddField(
            model_name='voting',
            name='slug_en',
            field=models.SlugField(blank=True, max_length=80, verbose_name='Voting URL slug'),
        ),
        migrations.AddField(
            model_name='voting',
            name='slug_fr',
            field=models.SlugField(blank=True, max_length=80, verbose_name='Voting URL slug'),
        ),
        migrations.AddField(
            model_name='voting',
            name='slug_it',
            field=models.SlugField(blank=True, max_length=80, verbose_name='Voting URL slug'),
        ),
        migrations.AddField(
            model_name='voting',
            name='slug_rm',
            field=models.SlugField(blank=True, max_length=80, verbose_name='Voting URL slug'),
        ),
    ]