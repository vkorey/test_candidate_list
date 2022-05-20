from django.contrib import admin

from .models import Skill, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Tag, TagAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("pk", "tag", "name")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Skill, SkillAdmin)
