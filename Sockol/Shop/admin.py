from django.contrib import admin
from Shop.models import *

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category_product', 'ref1', 'volume1', 'ref2', 'volume2')
    search_fields = ('name', 'ref1', 'ref2')

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Volume1)
admin.site.register(Volume2)
admin.site.register(Shop, ShopAdmin)


