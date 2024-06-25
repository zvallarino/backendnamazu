from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'zipcode', 'newsletter', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('zipcode', 'newsletter')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'zipcode', 'newsletter')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)