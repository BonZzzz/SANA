# Generated by Django 3.1.2 on 2020-10-23 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201023_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio',
            old_name='time',
            new_name='utime',
        ),
    ]
