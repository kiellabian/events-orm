# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from events.utils import ReadOnlyAdmin

from models import Event, EventDonation


class EventAdmin(ReadOnlyAdmin):
    list_display = ('title', 'owner')

    def get_queryset(self, request):
        return Event.objects.order_by('pk')


class EventDonationAdmin(ReadOnlyAdmin):
    list_display = ('owner', 'event', 'amount')

    def get_queryset(self, request):
        return EventDonation.objects.order_by('pk')


admin.site.register(Event, EventAdmin)
admin.site.register(EventDonation, EventDonationAdmin)
