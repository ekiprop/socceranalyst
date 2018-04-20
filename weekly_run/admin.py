from django.contrib import admin
from .models import Weeklymain, Weeklysub


class WeeklysubInline(admin.StackedInline):
    model = Weeklysub
    extra = 3


class WeeklymainAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['slip_name']}),
                 ('Date information', {'fields': ['slip_date'], 'classes': ['']}), ]
    inlines = [WeeklysubInline]

    list_display = ('slip_name', 'slip_date', 'recent_slips')


admin.site.register(Weeklymain, WeeklymainAdmin)
