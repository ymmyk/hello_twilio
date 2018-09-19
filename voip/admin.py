from django.contrib import admin

from voip.models import Call, Number

@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    pass

@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    pass
