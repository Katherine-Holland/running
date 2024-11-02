from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here. Register Post with PostAdmin customization
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
