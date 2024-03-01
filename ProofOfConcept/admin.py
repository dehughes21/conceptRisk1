from .models import Squirrel
from .models import User
from .models import Sighting
from django.contrib import admin

class SquirrelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Squirrel, SquirrelAdmin)
admin.site.register(User)
admin.site.register(Sighting)
