# Generated by Django 2.1.2 on 2018-11-11 00:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0009_auto_20181110_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 11, 11, 0, 11, 51, 679628, tzinfo=utc)),
        ),
    ]