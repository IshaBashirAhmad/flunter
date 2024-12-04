# Generated by Django 4.2.11 on 2024-11-01 06:34

from django.conf import settings
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
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='searches', to=settings.AUTH_USER_MODEL),
        ),
    ]