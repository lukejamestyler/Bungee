# Generated by Django 3.0.6 on 2020-05-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need', '0005_order_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
