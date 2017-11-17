# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Event
from utils import ReadOnlyAdmin


class EventAdmin(ReadOnlyAdmin):
    list_display = ('title', 'owner')

    def get_queryset(self, request):
        return Event.objects.order_by('pk')


admin.site.register(Event, EventAdmin)
