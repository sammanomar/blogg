from django.contrib import admin

from .models import *

from django_summernote.admin import SummernoteModelAdmin

@admin.register(Blog)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
