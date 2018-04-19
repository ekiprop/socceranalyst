from django.contrib import admin
from .models import DailyMain, DailySub


class DailySubInline(admin.StackedInline):
    model = DailySub
    extra = 3


class DailyMainAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['slip_name']}),
                 ('Date information', {'fields': ['slip_date'], 'classes': ['collapse']}), ]
    inlines = [DailySubInline]

    list_display = ('slip_name', 'slip_date', 'recent_slips')


admin.site.register(DailyMain, DailyMainAdmin)
