from django.contrib import admin

# Register your models here.
from main.models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'menu_name')

admin.site.register(Menu, MenuAdmin)
