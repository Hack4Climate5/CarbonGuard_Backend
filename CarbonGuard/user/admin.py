from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "username",
        "email",
        "password",
    )


admin.site.register(User, UserAdmin)
