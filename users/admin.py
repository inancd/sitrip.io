from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import profileModel

# Register your models here.

admin.site.unregister(Group)

class profileInlie(admin.StackedInline):
    model = profileModel

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "password", "email",]
    inlines = [profileInlie]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(profileModel)

