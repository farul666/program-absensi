from django.contrib import admin
from .models import *

class kolomdata(admin.ModelAdmin):
    list_display = ['nama','tgl','keterangan']
    search_fields = ['nama']
    list_filter = ('nama',)
    list_per_page = 7

admin.site.register(Perizinan,kolomdata)