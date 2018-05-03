# Generated by Django 2.0.1 on 2018-03-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ultramain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slip_date', models.DateTimeField(verbose_name='slip_date')),
                ('slip_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ultrasub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default=None, max_length=30)),
                ('home_team', models.CharField(max_length=30)),
                ('away_team', models.CharField(max_length=30)),
                ('prediction', models.CharField(max_length=40)),
                ('outcome', models.CharField(blank=True, max_length=20, null=True)),
                ('match_date', models.DateTimeField(verbose_name='match date')),
                ('daily_main', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ultra_odds.Ultramain')),
            ],
        ),
    ]
