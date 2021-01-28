from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

