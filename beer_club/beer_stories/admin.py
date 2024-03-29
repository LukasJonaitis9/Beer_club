from django.contrib import admin
from . import models


class TypeAdmin(admin.ModelAdmin):
    list_display = ['kinds', 'name', 'owner']
    list_display_links = ['kinds']
    list_filter = ['owner']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'rating', 'color', 'filtered', 'description', 'image', 'date']
    list_filter = ['type', 'rating', 'color']



admin.site.register(models.Type, TypeAdmin)
admin.site.register(models.Review, ReviewAdmin)