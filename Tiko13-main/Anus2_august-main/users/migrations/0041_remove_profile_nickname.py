# Generated by Django 4.2.1 on 2023-11-06 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_remove_webpagesettings_profile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
    ]