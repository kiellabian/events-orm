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
    when_created = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(
        User, related_name='participated_events')
    expected_donation_goal = models.FloatField(default=0.0)

    status = models.PositiveIntegerField(
        choices=EVENT_STATUS_CHOICES, default=0)
    when_registration_start = models.DateTimeField(null=True, blank=True)
    when_registration_end = models.DateTimeField(null=True, blank=True)
    when_event_start = models.DateTimeField(null=True, blank=True)
    when_event_end = models.DateTimeField(null=True, blank=True)


class EventDonation(models.Model):
    owner = models.ForeignKey(User, related_name='donations')
    event = models.ForeignKey(Event, related_name='donations')
    amount = models.FloatField(default=0.0)
