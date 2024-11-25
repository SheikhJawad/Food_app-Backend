from django.contrib import admin
from .models import *
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  
    search_fields = ('title', 'description')  
    ordering = ('title',)  
    list_filter = ('title',) 

class ChildItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'price', 'image')  
    list_filter = ('parent', 'price') 
    search_fields = ('title', 'description')  
    ordering = ('price',) 

admin.site.register(ParentCategory, ParentCategoryAdmin)
admin.site.register(ChildItem, ChildItemAdmin)
admin.site.register(Reservation)
admin.site.register(UserToken)
