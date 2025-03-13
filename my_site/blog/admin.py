from django.contrib import admin

# Register your models here.

from .models import Author, Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags","date")
    list_display = ("title", "date", "author")

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
