from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'author', 'message', 'timestamp']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']