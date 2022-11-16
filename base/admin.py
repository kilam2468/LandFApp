from django.contrib import admin

# Register your models here.

from .models import Room, School, Message, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(School)
admin.site.register(Message)
