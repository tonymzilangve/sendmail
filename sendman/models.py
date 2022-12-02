# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    list = models.ManyToManyField('SubscriberList', blank=True, verbose_name="Список")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        ordering = ['id']


class SubscriberList(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    subscribers = models.TextField(max_length=2000, blank=True, verbose_name="Подписчики")
    number = models.IntegerField(default=0, blank=True, null=True, verbose_name="Кол-во")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список подписчиков'
        verbose_name_plural = 'Списки подписчиков'
        ordering = ['-created_at']


class Template(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    subject = models.CharField(max_length=50, verbose_name="Тема")
    file = models.FileField(upload_to='media/templates/', help_text=".html", verbose_name="Макет (.html)")

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = 'Макет'
        verbose_name_plural = 'Макеты'
        ordering = ['name']


class SendHistory(models.Model):
    template = models.ForeignKey('Template', on_delete=models.PROTECT, verbose_name="Макет")
    rcpt_list = models.ForeignKey('SubscriberList', on_delete=models.PROTECT, verbose_name="Адресат")
    created_at = models.DateTimeField(auto_now_add=True)
    schedule = models.CharField(max_length=50, null=True, blank=True, verbose_name="Повтор")

    def __str__(self):
        return self.template + " to " + self.rcpt_list

    class Meta:
        verbose_name = 'История отправок'
        verbose_name_plural = 'Истории отправок'
        ordering = ['-created_at']
