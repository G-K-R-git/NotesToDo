# Generated by Django 3.1.7 on 2021-04-12 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20210412_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='urgent',
            field=models.BooleanField(default=0, verbose_name='Важно или нет'),
        ),
        migrations.AlterField(
            model_name='note',
            name='date_complete',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 0, 26, 6, 621642), verbose_name='Когда выполнить'),
        ),
    ]
