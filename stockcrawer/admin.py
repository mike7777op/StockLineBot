from django.contrib import admin
from .models import UserInfo, UserInfo2

# Register your models here.

class UserInfo_Admin(admin.ModelAdmin):
    list_display = ('uid','name')

class UserInfo2_Admin(admin.ModelAdmin):
    list_display = ('uid','name','days')


admin.site.register(UserInfo, UserInfo_Admin)
admin.site.register(UserInfo2, UserInfo2_Admin)
