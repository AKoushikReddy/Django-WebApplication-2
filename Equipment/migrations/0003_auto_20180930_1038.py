# Generated by Django 2.0.2 on 2018-09-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipment', '0002_auto_20180930_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sensoralarm',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]