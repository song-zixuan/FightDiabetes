# Generated by Django 3.2.5 on 2022-12-19 08:30

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_patientinfo_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports_record',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(
                2022, 12, 19, 16, 30, 57, 968411), verbose_name='日期时间'),
        ),
    ]
