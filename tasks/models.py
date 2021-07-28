from django.db import models
from django.db.models import Model
from django.utils.translation import gettext
from statuses.models import Status
from django.contrib.auth.models import User
from labels.models import Label


class Task(Model):
    name = models.CharField(
        max_length=100,
        verbose_name=gettext('Имя'),
        unique=True,
    )
    description = models.TextField(
        max_length=500,
        blank=True,
        verbose_name=gettext('Описание'),
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=gettext('Статус'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="task_executor",
        null=True,
        blank=True,
        verbose_name=gettext('Исполнитель'),
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_creator',
        null=True,
    )
    added_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(
        Label,
        blank=True,
        verbose_name=gettext('Метки'),
    )

    def __str__(self):
        return self.name
