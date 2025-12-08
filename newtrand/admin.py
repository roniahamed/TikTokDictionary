from django.contrib import admin
from .models import Category, NewTrandModel



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(NewTrandModel)
class NewTrandModelAdmin(admin.ModelAdmin):
    list_display = ('word', 'category', 'source', 'is_category', 'created_at', 'updated_at')
    list_filter = ('is_category', 'created_at', 'updated_at', 'category')
    search_fields = ('word', 'definition', 'example_sentence', 'source')
    ordering = ('-created_at', 'word')
