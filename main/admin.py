from django.contrib import admin
from django import forms

from .models import *

class AutoSlug(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(category, AutoSlug)
admin.site.register(catalog, AutoSlug)
admin.site.register(sub_category, AutoSlug)
admin.site.register(collection, AutoSlug)
#admin.site.register(Sizes)
admin.site.register(Furnite_category, AutoSlug)
admin.site.register(Furnite_sub_category, AutoSlug)
admin.site.register(Furnite)
admin.site.register(News)