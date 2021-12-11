from django.contrib import admin
from .models import Albums, Songs

class SongsInLine(admin.StackedInline):
    model = Songs
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Description', {'fields': ['description']})
    ]
    inlines = [SongsInLine]
    
admin.site.register(Albums, AlbumAdmin)