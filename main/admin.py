from django.contrib import admin
from .models import Books


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available', 'borrowed_by', 'borrowed_by_name')

    def borrowed_by_name(self, obj):
        if obj.borrowed_by:
            return f"{obj.borrowed_by.first_name} {obj.borrowed_by.last_name} ({obj.borrowed_by.username})"
        return "Не занята"
    borrowed_by_name.short_description = "Взята пользователем"
