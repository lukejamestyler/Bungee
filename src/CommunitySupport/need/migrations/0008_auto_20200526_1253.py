# Generated by Django 3.0.6 on 2020-05-26 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0007_auto_20200526_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='donations',
            new_name='donation',
        ),
    ]
