# Generated by Django 4.2.11 on 2024-06-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_subscription_remaining_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='customplan',
            name='remaining_credits',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
