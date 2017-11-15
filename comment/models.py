# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments')
    content = models.TextField()
