from django.contrib import admin

from ads.models import Comment, Ad


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("pk", "author", "text")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = ("pk", "author", "title", "price")
