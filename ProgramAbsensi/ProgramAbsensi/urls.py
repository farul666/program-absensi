"""
URL configuration for absensi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from absensi.views import *
from biodata.views import *
from perizinan.views import *
from presensi.views import *
from rekapitulasi.views import *
from users.views import *

urlpatterns = [
    # Route untuk Biodata
    path('admin/', admin.site.urls),
    path('home/', views.index),

    #CRUD Absensi
    path('absensi/',data_absensi),
    path('tambahabsensi/',tambah_absensi),
    path('hapus_absen/<int:id_absen>',hapus_absensi,name='hapus_absensi'),

    # CRUD Biodata
    path('biodata/', data),
    path('tambahbd/',tambahdt),
    path('ubahdt/<int:id_biodata>',update_dt,name='update_dt'), 
    path('hapusdt/<int:id_biodata>',hapusdt,name='hapusdt'),

    # CRUD Perizinan
    path('perizinan/',data_izin),
    path('tambahizin/',add_izin),
    path('ubahizin/<int:id_perizinan>',update_izin,name='update_izin'),
    path('hapusizin/<int:id_perizinan>',hapus_izin,name='hapus_izin'),

    #CRUD presensi
    path('presensi/',presensi),
    path('tambahpre/',tambahpresensi),
    path('hapuspre/<int:id_presensi>',hapuspresensi,name='hapuspresensi'),

    #CRUD presensi Pulang
    path('presensipulang/',presensipulang),
    path('tambahpreplg/',tambahpresensipulang),
    path('hapuspreplg/<int:id_presensi>',hapuspresensipulang,name='hapuspresensi'),

    # CRUD Laporan
    path('laporan/',rekap_data),
    # path('cetaklpr',cetaklpr),

    # Login and Register
    path('register/',views.daftar),
    path('',views.masuk),
    path('logout/',views.keluar),

    # Path dibawah ini berfungsi untuk memasukkan urls pada app authentication
    path('',include('django.contrib.auth.urls')),

    # Path User
    path('user/',homeuser),
    path('presensiuser/',presensiuser),
    path('presensipulanguser/',presensipulanguser),
    path('absensiuser/',absensiiuser),
    path('perizinanuser/',perizinanuser),
    
]
