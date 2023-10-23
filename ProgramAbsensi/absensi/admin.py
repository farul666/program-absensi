from django.contrib import admin
from .models import *

class kolomdata(admin.ModelAdmin):
    list_display = ['nama','tgl','status']
    search_fields = ['nama']
    list_filter = ('nama',)
    list_per_page = 7

admin.site.register(Absen,kolomdata)