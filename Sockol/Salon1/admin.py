from django.contrib import admin
from .models import *

class Laser_epilationAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'gender', 'price')

admin.site.register(Icon)
admin.site.register(Gender)
admin.site.register(Laser_epilation, Laser_epilationAdmin)
admin.site.register(Category_service)
admin.site.register(Type_service)
