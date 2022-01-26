from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug'
    list_filter = ['price']
    prepopulated_fields = {'slug': ('name', )}

# Register your models here.
