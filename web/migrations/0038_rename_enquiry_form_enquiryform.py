# Generated by Django 4.2 on 2023-09-09 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_rename_form_enquiry_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Enquiry_Form',
            new_name='EnquiryForm',
        ),
    ]