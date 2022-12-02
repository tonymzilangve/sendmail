from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emailp2.settings")

app = Celery("emailp2")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-15-minutes': {
        'task': 'send_mail_task',
        'schedule': crontab(minute='*/15'),
        'args': (2, 2)
    }
}


