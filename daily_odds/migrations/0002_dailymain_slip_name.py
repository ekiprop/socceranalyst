# Generated by Django 2.0.1 on 2018-03-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_odds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailymain',
            name='slip_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
