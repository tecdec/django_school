# Generated by Django 2.1.2 on 2018-11-02 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='answer',
        ),
    ]
