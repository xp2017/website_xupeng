# Generated by Django 2.1.5 on 2019-02-08 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20190208_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 13, 16, 0, 288645, tzinfo=utc)),
        ),
    ]
