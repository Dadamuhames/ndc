# Generated by Django 4.1 on 2023-02-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projects_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
