from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# admin 패널에서 User를 보고싶을 때 등록을 함
# 밑에 클래스가  User에서 사용될 클래스
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "CustomProfile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthDate",
                    "curruncy",
                    "language",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "curruncy",
        "superhost",
        "avatar",
        "gender",
        "bio",
        "birthDate",
        "email_verified",
        "email_secret",
        "login_method",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

