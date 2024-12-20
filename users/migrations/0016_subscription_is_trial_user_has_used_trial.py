# Generated by Django 4.2.11 on 2024-06-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_customplan_last_payment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='is_trial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='has_used_trial',
            field=models.BooleanField(default=False),
        ),
    ]
