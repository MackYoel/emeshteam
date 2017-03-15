from django.contrib import admin
from .models import Person, Score


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'pk',)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'person', 'pk',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Score, ScoreAdmin)
