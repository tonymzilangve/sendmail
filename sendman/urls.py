# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Sendman.as_view(), name="send_email"),

    url(r'^recipients/$', ShowLists.as_view(), name="recipients"),
    url(r'^recipients/(?P<pk>\d+)', showList, name="rcpt_list"),
    url(r'^recipients/add', newList, name="new_recipients"),
    url(r'^recipients/delete/(?P<pk>\d+)', deleteList, name="delete_list"),

    url(r'^template/new', NewTemplate.as_view(), name="new_template"),
    url(r'^template/all', ShowTemplates.as_view(), name="templates"),
    url(r'^template/delete/(?P<pk>\d+)', deleteTemplate, name="delete_template"),

    url(r'^history', ShowHistory.as_view(), name="history"),
]
