# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


EVENT_STATUS_CHOICES = (
    (0, 'On Hold'),
    (1, 'Registration'),
    (2, 'Waiting for Event to Start'),
    (3, 'On Going'),
    (4, 'Finished')
)


class Event(models.Model):
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(User, related_name='events')
    removed = models.BooleanField(default=False)
    participants = models.ManyToManyField(
        User, related_name='participated_events')

    status = models.PositiveIntegerField(
        choices=EVENT_STATUS_CHOICES, default=0)
    when_registration_start = models.DateTimeField(null=True, blank=True)
    when_registration_end = models.DateTimeField(null=True, blank=True)
    when_event_start = models.DateTimeField(null=True, blank=True)
    when_event_end = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class EventDonation(models.Model):
    owner = models.ForeignKey(User, related_name='donations')
    event = models.ForeignKey(Event, related_name='donations')
    amount = models.FloatField(default=0.0)

    def __unicode__(self):
        return '{0} donated ${1} to {2}'.format(
            self.owner, self.amount, self.event)
