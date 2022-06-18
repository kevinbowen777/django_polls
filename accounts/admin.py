from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] = fieldsets[1][1]["fields"] + (
        "country",
        "profile_pic",
        "bio",
    )
    """
    fieldsets = UserAdmin.fieldsets + (
        ('Personal info', {'fields': ('country', 'bio', 'profile_pic',)}),
                )
    """


admin.site.register(CustomUser, CustomUserAdmin)
