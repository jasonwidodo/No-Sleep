# Generated by Django 4.1 on 2022-12-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
