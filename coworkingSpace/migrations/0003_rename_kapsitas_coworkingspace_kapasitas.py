# Generated by Django 4.1 on 2022-12-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coworkingSpace', '0002_coworkingspace_favorit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coworkingspace',
            old_name='kapsitas',
            new_name='kapasitas',
        ),
    ]
