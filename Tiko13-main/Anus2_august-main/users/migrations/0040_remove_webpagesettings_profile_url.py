# Generated by Django 4.2.1 on 2023-09-13 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_remove_profile_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpagesettings',
            name='profile_url',
        ),
    ]
