# Generated by Django 4.2.11 on 2024-06-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_payment_method_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user_payment_method_id',
        ),
    ]
