# Generated by Django 4.2.11 on 2024-11-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_subscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]