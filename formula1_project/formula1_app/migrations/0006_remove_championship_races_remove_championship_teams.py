# Generated by Django 5.0 on 2023-12-30 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula1_app', '0005_championship_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='championship',
            name='races',
        ),
        migrations.RemoveField(
            model_name='championship',
            name='teams',
        ),
    ]