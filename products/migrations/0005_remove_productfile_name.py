# Generated by Django 3.1.4 on 2020-12-12 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201212_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfile',
            name='name',
        ),
    ]
