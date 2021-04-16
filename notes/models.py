from django.db import models
from django.contrib.auth.models import User
import datetime


class Note(models.Model):
    STATUSES = ((0, 'Выполнено'),
                (1, 'Активно'),
                (2, 'Отложено'),
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(default='', verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, editable=False)
    date_add = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    date_complete = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=1)),
                                         verbose_name='Когда выполнить')
    public = models.BooleanField(default=False, verbose_name='Публичная')
    status = models.IntegerField(default=1, choices=STATUSES, verbose_name='Статус задачи')
    urgent = models.BooleanField(default=0, verbose_name='Важно или нет')

    def __str__(self):
        return {
            'id': self.id, 'title': self.title, 'datetime': str(self.date_add)
        }
