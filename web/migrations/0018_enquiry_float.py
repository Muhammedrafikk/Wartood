# Generated by Django 4.2.3 on 2023-08-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_remove_enquiry_float'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='float',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]