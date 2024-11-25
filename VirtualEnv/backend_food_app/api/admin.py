from django.contrib import admin
from .models import *
admin.site.register(Reservation)
admin.site.register(UserToken)
# admin.site.register(MenuItem)
admin.site.register(ParentCategory)
admin.site.register(ChildItem)

