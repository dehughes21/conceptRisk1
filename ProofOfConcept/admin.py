from .models import Squirrel
from django.contrib import admin

class SquirrelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Squirrel, SquirrelAdmin)
