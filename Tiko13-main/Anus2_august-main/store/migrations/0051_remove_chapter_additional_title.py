# Generated by Django 4.2.1 on 2023-11-05 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0050_book_last_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='additional_title',
        ),
    ]