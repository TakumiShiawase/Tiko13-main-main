# Generated by Django 4.2.1 on 2023-08-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_alter_profile_auto_add_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='library_privacy',
            field=models.CharField(choices=[('nobody', 'Nobody'), ('followers', 'Only Followers'), ('friends', 'Only Friends'), ('anyone', 'Anyone')], default='anyone', max_length=10),
        ),
    ]
