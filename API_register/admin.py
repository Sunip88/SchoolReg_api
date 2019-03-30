from django.contrib import admin

from API_register.models import Classes, Teacher, Announcements


@admin.register(Classes)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'educator', 'name', 'description']


@admin.register(Teacher)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


def content_display_thirty_signs(obj):
    return str(obj.text)[:30]


content_display_thirty_signs.short_description = 'text'


def hidden(model_admin, request, query_set):
    query_set.update(hidden=True)


hidden.short_description = "Ukryj element w widoku"


@admin.register(Announcements)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'classes', 'date', content_display_thirty_signs, 'author', 'hidden']
    list_filter = ['hidden', 'classes']
    actions = [hidden, ]
