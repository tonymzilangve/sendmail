# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', u'name', u'surname', 'email')
    list_display_links = ('id', 'email')
    search_fields = (u'name', u'surname', 'email')
    list_filter = ('email',)


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', u'name', 'created_at')
    search_fields = (u'name',)
    list_filter = (u'name',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', u'name', u'subject')
    list_display_links = ('id', u'name')
    search_fields = (u'name', u'subject')


class SendHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', u'template', u'rcpt_list', 'created_at', 'schedule')
    list_display_links = ('id', u'template', u'rcpt_list')
    search_fields = (u'template', u'rcpt_list')
    list_filter = (u'template', u'rcpt_list', )


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriberList, ListAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(SendHistory, SendHistoryAdmin)
