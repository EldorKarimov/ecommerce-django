from django.contrib import admin

from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'is_admin', 'is_staff', 'is_active', 'is_superadmin', 'date_joined', 'last_login']
    search_fields = ('first_name', 'last_name', 'username')
    readonly_fields = ('date_joined', 'last_login')

    ordering = ('-pk', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()