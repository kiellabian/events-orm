from random import randrange

from datetime import datetime
from django.utils.timezone import timedelta
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin

from models import Event, EventDonation


class ReadOnlyAdmin(ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


def random_time():
    return timedelta(
        hours=randrange(7) - 3,
        minutes=randrange(61) - 30
    )


def create_users():
    for i in xrange(1, 1001):
        User.objects.create(
            username='user' + str(i),
            password='password'
        )


def create_events():
    date = datetime(2017, 11, 17, 21)
    for status in xrange(5):
        for i in xrange(200 * status + 1, 200 * (status + 1) + 1):
            Event.objects.create(
                title='Event ' + str(i),
                owner_id=randrange(1, 101),
                status=status,
                when_registration_start=date + random_time(),
                when_registration_end=date + random_time() + timedelta(days=1),
                when_event_start=date + random_time() + timedelta(days=2),
                when_event_end=date + random_time() + timedelta(days=3),
            )
        date -= timedelta(days=1)


def add_participants():
    for event in Event.objects.all():
        participant_count = randrange(101)
        for p in xrange(participant_count):
            event.participants.add(User.objects.get(id=randrange(1, 1001)))


def add_donations():
    for event in Event.objects.all():
        donation_count = randrange(101)
        for p in xrange(donation_count):
            EventDonation.objects.create(
                owner_id=randrange(1, 1001),
                event=event,
                amount=randrange(1, 20)
            )
