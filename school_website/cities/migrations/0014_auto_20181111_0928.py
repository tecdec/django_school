# Generated by Django 2.1.2 on 2018-11-11 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0013_auto_20181111_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 11, 11, 9, 28, 50, 352379, tzinfo=utc)),
        ),
    ]
