# Generated by Django 4.2.11 on 2024-11-05 07:44

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saved_searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searches',
            name='search_via',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('email1', 'Email 1'), ('email2', 'Email 2'), ('phone1', 'Phone 1'), ('phone2', 'Phone 2')], max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='searches',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='searches', to=settings.AUTH_USER_MODEL),
        ),
    ]