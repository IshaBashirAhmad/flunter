# Generated by Django 4.2.11 on 2024-05-30 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='company_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
            preserve_default=False,
        ),
    ]
