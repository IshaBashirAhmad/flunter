# Generated by Django 4.2.11 on 2024-06-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_temporarysubscriptiondata'),
    ]

    operations = [
        migrations.AddField(
            model_name='customplan',
            name='last_payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customplan',
            name='next_payment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
