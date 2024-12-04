# Generated by Django 4.2.11 on 2024-10-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_alter_profileactions_action_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileactions',
            name='action_type',
            field=models.CharField(choices=[('call', 'call'), ('text_message', 'text messages'), ('voice_email', 'voice email'), ('email', 'email'), ('note', 'note'), ('convert', 'convert')], max_length=100),
        ),
    ]
