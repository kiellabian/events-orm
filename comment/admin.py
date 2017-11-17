# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from events.utils import ReadOnlyAdmin
from models import Comment


class CommentAdmin(ReadOnlyAdmin):
    list_display = ('owner', 'content')

    def get_queryset(self, request):
        return Comment.objects.order_by('pk')


admin.site.register(Comment, CommentAdmin)
