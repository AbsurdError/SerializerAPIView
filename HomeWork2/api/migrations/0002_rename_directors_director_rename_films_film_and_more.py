# Generated by Django 5.0.1 on 2024-01-16 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Directors',
            new_name='Director',
        ),
        migrations.RenameModel(
            old_name='Films',
            new_name='Film',
        ),
        migrations.RenameModel(
            old_name='Posters',
            new_name='Poster',
        ),
        migrations.RenameModel(
            old_name='Styles',
            new_name='Style',
        ),
    ]
