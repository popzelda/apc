# Generated by Django 3.2.2 on 2022-10-30 19:41

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_n', models.URLField()),
                ('photo_n', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[200, 600], upload_to='')),
                ('desc_n', models.CharField(max_length=250)),
                ('created_n', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requette_a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(blank=True, max_length=150, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('lettre', models.TextField(blank=True, max_length=500, null=True)),
                ('join_f', models.FileField(blank=True, null=True, upload_to='requette')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='list_ch',
            field=models.CharField(choices=[('association', 'مجتمع مدني'), ('employe', 'موظف في البلدية'), ('cartiers', ' رئيس حي'), ('organisme', 'هيئة نظامية'), ('citoyen', 'مواطن')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requette_u',
            name='Titre',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requette_u',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requette_u',
            name='created_r',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requette_u',
            name='lettre',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='requette_u',
            name='lot_terrain',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv_user',
            field=models.FileField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to=''),
        ),
        migrations.AlterField(
            model_name='requette_u',
            name='join_f',
            field=models.FileField(blank=True, null=True, upload_to='requette'),
        ),
        migrations.AlterField(
            model_name='requette_u',
            name='userr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
