from django.contrib import admin

from voip.models import Calls, Number

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    pass

@admin.register(Calls)
class CallAdmin(admin.ModelAdmin):
    pass
