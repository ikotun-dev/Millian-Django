# Generated by Django 4.1.5 on 2023-01-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnstuff', '0004_rename_bookstem_book_stem'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_stem',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50), unique=True),
        ),
    ]
