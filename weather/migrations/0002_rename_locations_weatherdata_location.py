# Generated by Django 5.1.7 on 2025-03-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='locations',
            new_name='location',
        ),
    ]
