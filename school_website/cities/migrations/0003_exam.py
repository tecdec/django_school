# Generated by Django 2.1.2 on 2018-11-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20181102_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('allowed_time_mins', models.IntegerField(default=10)),
            ],
        ),
    ]
