# Generated by Django 4.2 on 2023-09-08 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_rename_serviceform_service_conact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='service_conact',
            new_name='serviceform',
        ),
    ]
