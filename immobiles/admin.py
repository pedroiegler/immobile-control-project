from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.RegisterLocation)

class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImmobileImage
    extra = 0

class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]

admin.site.register(models.Immobile, ImmobileAdmin)