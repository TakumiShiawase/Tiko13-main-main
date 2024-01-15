# Generated by Django 4.2.1 on 2023-07-16 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0030_book_abstract_book_author_remark_book_is_adult'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='co_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coauthored_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('finished', 'Finished'), ('draft', 'Draft')], default='in_progress', max_length=20),
        ),
    ]