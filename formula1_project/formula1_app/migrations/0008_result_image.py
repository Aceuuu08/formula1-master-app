# Generated by Django 5.0 on 2023-12-31 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1_app', '0007_driver_image_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/drivers'),
        ),
    ]
