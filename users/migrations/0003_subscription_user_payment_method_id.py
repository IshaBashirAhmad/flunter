# Generated by Django 4.2.11 on 2024-05-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_superadmin_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user_payment_method_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
