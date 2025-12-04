from django.contrib import admin
from .models import User
from unfold.admin import ModelAdmin

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'profile_image', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('username',)    
