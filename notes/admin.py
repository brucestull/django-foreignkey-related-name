from django.contrib import admin

from .models import Explanation, Note, Profile


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    search_fields = ("title", "content")
    list_filter = ("user",)
    ordering = ("-id",)


@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    list_display = ("name", "truncated_description")
    search_fields = ("name", "description")
    ordering = ("-id",)

    def truncated_description(self, obj):
        return (
            obj.description[:50] + "..."
            if len(obj.description) > 50
            else obj.description
        )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("nickname", "user")
    search_fields = ("nickname", "bio")
    list_filter = ("user",)
    ordering = ("-id",)


# Register your models here.
