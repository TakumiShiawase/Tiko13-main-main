# Generated by Django 4.2.1 on 2023-11-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_remove_webpagesettings_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpagesettings',
            name='gender',
            field=models.CharField(blank=True, choices=[('not_specified', 'Not Specified'), ('female', 'Female'), ('male', 'Male'), ('other', 'Other')], default='not_specified', max_length=15),
        ),
    ]
