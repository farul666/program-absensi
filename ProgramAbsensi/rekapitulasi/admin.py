from django.contrib import admin
from .models import *

class kolomdata(admin.ModelAdmin):
    list_display = ['id', 'nama','absen_id','presensi_id','perizinan_id']
    search_fields = ['nip','nama']
    list_filter = ['nama']
    list_per_page = 7

admin.site.register(Rekap,kolomdata)