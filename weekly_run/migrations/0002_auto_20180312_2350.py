# Generated by Django 2.0.1 on 2018-03-12 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_run', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklysub',
            old_name='daily_main',
            new_name='weekly_main',
        ),
    ]
