# Generated by Django 4.1 on 2023-02-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_projects_image_first_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='serivices',
            new_name='services',
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.JSONField(blank=True, null=True, verbose_name='Descr'),
        ),
    ]
