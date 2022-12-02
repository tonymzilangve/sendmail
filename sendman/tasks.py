# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Engine, Context

from celery import shared_task
from .models import *
from dotenv import load_dotenv

import smtplib


from email.mime.text import MIMEText
from email.utils import formatdate

load_dotenv()


def render_template(template, context):
    engine = Engine.get_default()
    tmpl = engine.get_template(template)
    return tmpl.render(Context(context))


@shared_task(bind=True, name="send_mail_task")
def send_mail_task(request, template_id, rcpt_list_id):
    server = smtplib.SMTP(os.getenv('EMAIL_HOST'), os.getenv('EMAIL_PORT'))
    server.starttls()

    try:
        server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
    except Exception as e:
        return "{}\nПроверьте данные отправителя!".format(e)

    template = Template.objects.get(pk=template_id)

    recipients = Subscriber.objects.filter(list=rcpt_list_id).values()
    for user in list(recipients):
        email = user['email']
        name = user['name']
        surname = user['surname']

        context = {
            "subscriber": '{} {}'.format(name, surname)
        }

        msg = MIMEText(render_template(template.file.name, context).encode('utf-8', 'ignore'), "html")
        msg['From'] = os.getenv('EMAIL_HOST_USER')
        msg['To'] = email
        msg['Date'] = formatdate(localtime=True)
        msg["Subject"] = template.subject
        msg['X-Confirm-Reading-To'] = os.getenv('EMAIL_HOST_USER')
        server.sendmail(os.getenv('EMAIL_HOST_USER'), email, msg.as_string(), rcpt_options=['NOTIFY=SUCCESS,DELAY,FAILURE'])

    server.quit()
    return "Сообщение отправлено!"
