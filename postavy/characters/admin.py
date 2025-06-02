from django.contrib import admin
from .models import Postava

@admin.register(Postava)
class PostavaAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'rasa', 'trida', 'uroven', 'je_aktivni', 'datum_vytvoreni')
    list_filter = ('rasa', 'trida', 'je_aktivni', 'uroven')
    search_fields = ('jmeno', 'rasa', 'trida', 'zivotopis')
    # editace pole přímo v seznamu
    # list_editable = ('uroven', 'je_aktivni')

# Alternativní způsob registrace:
# admin.site.register(Postava, PostavaAdmin)