from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category)
admin.site.register(catalog)
admin.site.register(sub_category)
admin.site.register(collection)
#admin.site.register(Sizes)
admin.site.register(Furnite_category)
admin.site.register(Furnite_sub_category)
admin.site.register(Furnite)
admin.site.register(News)