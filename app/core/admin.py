from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#something about making it easier to work with multiple projects and PL
from django.utils.translation import gettext as _
from core import models
# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email','name']
    fieldsets= (
        (None,{'fields':('email', 'password')}),
        (('Personal Info'), {'fields': ('name',)}),
        (
            ('Persmissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('email', 'password1', 'password2')
        }),
    )
#don't remember exactly what UserAdmin does
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
