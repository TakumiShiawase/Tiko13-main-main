# Generated by Django 4.2.1 on 2023-07-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_illustration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
    ]
