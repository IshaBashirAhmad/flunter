# Generated by Django 4.2.11 on 2024-05-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_searches'),
    ]

    operations = [
        migrations.AddField(
            model_name='searches',
            name='number_of_results',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]