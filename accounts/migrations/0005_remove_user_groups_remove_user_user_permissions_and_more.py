# Generated by Django 4.1 on 2022-12-02 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_spaceadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='SpaceAdmin',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
