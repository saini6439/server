# Generated by Django 2.2.4 on 2019-10-20 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20191009_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='nickname',
        ),
    ]
