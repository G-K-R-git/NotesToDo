# Generated by Django 3.1.7 on 2021-04-12 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20210330_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='Когда выполнить',
        ),
        migrations.AddField(
            model_name='note',
            name='date_complete',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 23, 55, 41, 699252), verbose_name='Когда выполнить'),
        ),
    ]
