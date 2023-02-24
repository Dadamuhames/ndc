# Generated by Django 4.1 on 2023-02-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_alter_services_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='position',
            field=models.PositiveIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partners',
            name='position',
            field=models.PositiveIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='position',
            field=models.PositiveIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='position',
            field=models.PositiveIntegerField(default=1, verbose_name='Position'),
            preserve_default=False,
        ),
    ]
