# Generated by Django 4.2.11 on 2024-07-04 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_subscriptionplans_simultaneous_connections_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='last_activity',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
