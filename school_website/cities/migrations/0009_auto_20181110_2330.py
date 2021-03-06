# Generated by Django 2.1.2 on 2018-11-10 23:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0008_question_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 11, 10, 23, 30, 35, 666607, tzinfo=utc)),
        ),
    ]
