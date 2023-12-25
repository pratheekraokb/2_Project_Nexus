from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    list_display = ('email', 'name', 'age', 'is_active', 'is_staff')
    ordering = ('email',)

# Register your custom admin class
admin.site.register(UserProfile)
