from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
    list_display = ('Medidor', 'Coordenadas', 'created', 'completed')
    list_filter = ('important', 'completed')
    search_fields = ('Medidor', 'Coordenadas')

admin.site.register(Task, TaskAdmin)
