# Generated by Django 3.1.2 on 2020-10-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_audio_spec'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='prediction',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
