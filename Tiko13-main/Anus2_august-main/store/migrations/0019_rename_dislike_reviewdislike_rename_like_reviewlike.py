# Generated by Django 4.2.1 on 2023-06-21 03:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0018_like_dislike'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dislike',
            new_name='ReviewDislike',
        ),
        migrations.RenameModel(
            old_name='Like',
            new_name='ReviewLike',
        ),
    ]