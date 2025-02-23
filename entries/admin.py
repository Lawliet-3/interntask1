from django.contrib import admin
from .models import DataEntry

@admin.register(DataEntry)
class DataEntryAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', 'is_reviewed', 'timestamp')
    list_filter = ('category', 'is_reviewed')
    search_fields = ('content',)
    list_editable = ('is_reviewed',)
    date_hierarchy = 'timestamp'
