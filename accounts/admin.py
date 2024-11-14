from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_admin', 'is_pelanggan', 'gender')
    list_filter = ('is_staff', 'is_admin', 'is_pelanggan', 'gender')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informasi Pribadi', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'image', 'address', 'gender', 'birth_date')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_pelanggan')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_admin', 'is_pelanggan')
        }),
    )
    
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
