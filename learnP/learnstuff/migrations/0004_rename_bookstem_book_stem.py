# Generated by Django 4.1.5 on 2023-01-26 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnstuff', '0003_rename_book_bookstem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookstem',
            new_name='Book_stem',
        ),
    ]
