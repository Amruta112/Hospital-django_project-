# Generated by Django 5.0.6 on 2024-06-17 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Synergy', '0005_alter_addhospital_hospital_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addhospital',
            new_name='Hospital',
        ),
    ]
