# Generated by Django 2.0.7 on 2018-12-06 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181206_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion'),
        ),
    ]
