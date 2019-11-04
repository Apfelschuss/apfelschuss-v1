# Generated by Django 2.2.6 on 2019-11-04 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Poll category title')),
                ('slug', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll category URL slug')),
                ('poll_date', models.DateTimeField(verbose_name='Poll final date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_de', models.CharField(blank=True, max_length=160, verbose_name='Poll title')),
                ('title_fr', models.CharField(blank=True, max_length=160, verbose_name='Poll title')),
                ('title_it', models.CharField(blank=True, max_length=160, verbose_name='Poll title')),
                ('title_rm', models.CharField(blank=True, max_length=160, verbose_name='Poll title')),
                ('title_en', models.CharField(blank=True, max_length=160, verbose_name='Poll title')),
                ('slug_de', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll URL slug')),
                ('slug_fr', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll URL slug')),
                ('slug_it', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll URL slug')),
                ('slug_rm', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll URL slug')),
                ('slug_en', models.SlugField(blank=True, max_length=80, unique=True, verbose_name='Poll URL slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('description_de', tinymce.models.HTMLField(blank=True, verbose_name='Poll description')),
                ('description_fr', tinymce.models.HTMLField(blank=True, verbose_name='Poll description')),
                ('description_it', tinymce.models.HTMLField(blank=True, verbose_name='Poll description')),
                ('description_rm', tinymce.models.HTMLField(blank=True, verbose_name='Poll description')),
                ('description_en', tinymce.models.HTMLField(blank=True, verbose_name='Poll description')),
                ('thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Thumbnail')),
                ('video_url_de', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('video_url_fr', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('video_url_it', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('video_url_rm', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('video_url_en', models.URLField(blank=True, verbose_name='Youtube embedded URL')),
                ('admin_brochure_de', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('admin_brochure_fr', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('admin_brochure_it', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('admin_brochure_rm', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('admin_brochure_en', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Formal brochure')),
                ('official_pro', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Final result pro [%]')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured poll')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Author')),
                ('categories', models.ManyToManyField(to='polls.Category', verbose_name='Poll category')),
            ],
        ),
    ]
