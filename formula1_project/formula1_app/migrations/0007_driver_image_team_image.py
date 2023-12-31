# Generated by Django 5.0 on 2023-12-31 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1_app', '0006_remove_championship_races_remove_championship_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/drivers'),
        ),
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/teams'),
        ),
    ]
