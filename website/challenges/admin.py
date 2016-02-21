from django.contrib import admin
from .models import Challenge

# Register your models here.
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "numberOfResolutions")
    def numberOfResolutions(self, obj):
        return obj.numberOfResolutions()
    numberOfResolutions.short_description = "nombre de résolution"


