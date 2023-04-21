from django.contrib import admin
from .models import users
# Register your models here.


class users_admin(admin.ModelAdmin):
    list_display = ('username','email','password','phone','country','language',)


admin.site.register(users,users_admin)