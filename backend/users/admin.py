from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Follow, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email',)
    list_filter = ('email', 'first_name')
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    empty_value_display = '-пусто-'
