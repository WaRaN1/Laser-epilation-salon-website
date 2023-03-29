from django.contrib import admin
from .models import Promoution

class PromoutionAdmin(admin.ModelAdmin):
    list_display = ('date', 'gender', 'type', 'category', 'size')

admin.site.register(Promoution, PromoutionAdmin)
