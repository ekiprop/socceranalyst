# Generated by Django 2.0.1 on 2018-03-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_odds', '0003_dailysub_daily_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymain',
            name='slip_date',
            field=models.DateTimeField(verbose_name='slip_date'),
        ),
    ]
