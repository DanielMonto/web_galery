# Generated by Django 4.2.4 on 2023-08-27 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 27, 17, 40, 49, 541176)),
        ),
    ]