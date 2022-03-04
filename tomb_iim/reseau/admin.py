from django.contrib import admin

# Register your models here.

from .models import Posts

class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created_at', 'created_by', 'like']

admin.site.register(Posts, PostsAdmin)