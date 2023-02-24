# Generated by Django 4.1 on 2023-02-23 11:12

import admins.models
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_alter_staticinformation_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='rev_image')),
                ('title', models.JSONField(validators=[admins.models.json_field_validate], verbose_name='Title')),
                ('text', models.JSONField(blank=True, null=True, verbose_name='Text')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.RemoveField(
            model_name='partners',
            name='deckription',
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.JSONField(validators=[admins.models.json_field_validate], verbose_name='Title')),
                ('sub_title', models.JSONField(blank=True, null=True, verbose_name='Sub title')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='Price')),
                ('deckription', models.JSONField(blank=True, null=True, verbose_name='Deckription')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='service_images')),
                ('meta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.metatags')),
            ],
        ),
    ]
