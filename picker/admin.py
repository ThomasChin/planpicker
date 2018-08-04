from django.contrib import admin
from .models import Plan, Location

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_filter = ('price_point', 'location')

admin.site.register(Location)
admin.site.register(Plan, PlanAdmin)