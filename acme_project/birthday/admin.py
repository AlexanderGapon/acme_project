from django.contrib import admin
from .models import Birthday, Tag


admin.site.register(Birthday)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)