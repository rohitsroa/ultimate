from django.contrib import admin
from .models import User, UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import  UserAdminChangeForm, UserAdminCreationForm


# Register your models here.

#User = get_user_model()

#admin.site.register(User)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('userid', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('userid', 'password','department','rank',)}),
        ('Permissions', {'fields': ('admin','engineer','manager','active','staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userid', 'password1', 'password2','department','rank','active','staff','admin','manager','engineer',)}
        ),
    )
    search_fields = ('userid',)
    ordering = ('userid',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

