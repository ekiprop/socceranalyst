from django.contrib import admin
from .models import Ultramain, Ultrasub


class UltrasubInline(admin.StackedInline):
    model = Ultrasub
    extra = 3


class UltramainAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['slip_name']}),
                 ('Date information', {'fields': ['slip_date'], 'classes': ['collapse']}), ]
    inlines = [UltrasubInline]

    list_display = ('slip_name', 'slip_date', 'recent_slips')


admin.site.register(Ultramain, UltramainAdmin)
