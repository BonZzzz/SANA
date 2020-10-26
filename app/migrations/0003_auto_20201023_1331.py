# Generated by Django 3.1.2 on 2020-10-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201023_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='spec',
            field=models.ImageField(null=True, upload_to='spectrogram'),
        ),
    ]
