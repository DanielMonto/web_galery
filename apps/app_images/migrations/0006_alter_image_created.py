# Generated by Django 4.2.4 on 2023-08-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_images', '0005_alter_image_options_image_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
