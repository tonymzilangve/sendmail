# -*- coding: utf-8 -*-
from django import forms
from .tasks import *
from .models import *


class AddTemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = "__all__"


class AddSubscriberListForm(forms.ModelForm):
    class Meta:
        model = SubscriberList
        exclude = ['number']


class AddSubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['list']

