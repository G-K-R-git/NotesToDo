# Generated by Django 3.1.7 on 2021-03-30 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210330_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='date_complete',
        ),
        migrations.AddField(
            model_name='note',
            name='Когда выполнить',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 19, 6, 58, 553474)),
        ),
    ]