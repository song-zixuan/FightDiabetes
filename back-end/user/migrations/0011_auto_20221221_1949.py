# Generated by Django 3.2.5 on 2022-12-21 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20221221_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine_record',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 19, 49, 52, 566177), verbose_name='日期时间'),
        ),
        migrations.AlterField(
            model_name='sports_record',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 21, 19, 49, 52, 566000), verbose_name='日期时间'),
        ),
    ]
