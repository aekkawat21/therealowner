from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(UserProfile)

class ItemAdmin(admin.ModelAdmin):
    # Specifies the fields to be displayed in the list view
    list_display = (
        'brand', 
        'model', 
        'color', 
        'serial_number', 
        'category', 
        'store_date_of_purchase', 
        'store_of_purchase', 
        'warranty', 
        'previous_owner',
        'description',
    )

    # Optional: If you want to add filtering options on the side of the page
    list_filter = ('category', 'brand', 'store_of_purchase')

    # Optional: If you want to add a search bar to search within specified fields
    search_fields = ('brand', 'model', 'serial_number', 'previous_owner')

    # Optional: If you want to add hierarchy navigation by date
    date_hierarchy = 'store_date_of_purchase'

    # Optional: If you want to specify the default ordering
    ordering = ('-store_date_of_purchase',)

# Register the Item model and the custom ItemAdmin
admin.site.register(Item, ItemAdmin)
