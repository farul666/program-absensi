from django.shortcuts import render, redirect
from presensi.forms import *
from presensi.models import *
from django.contrib import messages
from biodata.models import Biodata

# method untuk menampilkan data pada app presensi
def presensi(request):
    presensi=Presensi.objects.all()
    biodata=Biodata.objects.all()

    konteks={
        'presensi':presensi,
        'biodata':biodata,
    }
    return render(request,'Back-end/Presensi/data_presensi.html',konteks)

def presensipulang(request):
    presensipulang=PresensiPulang.objects.all()
    biodata=Biodata.objects.all()

    konteks={
        'biodata':biodata,
        'presensipulang': presensipulang,
    }
    return render(request,'Back-end/PresensiPulang/data_presensi.html',konteks)

# method untuk menampilkan data pada taebel presensi
def tambahpresensi(request):
    form=FormPresensi(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPresensi()
        konteks ={
            'form': form
        }
        return render(request,'Back-end/Presensi/add_presensi.html',konteks)
    else:
        form=FormPresensi()
        konteks={
            'form':form
        }
    return render(request,'Back-end/Presensi/add_presensi.html',konteks)

# method untuk menghapusn data pada app presensi
def hapuspresensi(request,id_presensi):
    presensi =Presensi.objects.get(id=id_presensi)
    presensi.delete()
    messages.success(request,"Data berhasil dihapus")
    return redirect ('/presensi')

# Method untuk presensi pulang
def tambahpresensipulang(request):
    form=FormPresensiPulang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPresensiPulang()
        konteks ={
            'form': form
        }
        return render(request,'Back-end/PresensiPulang/add_presensi.html',konteks)
    else:
        form=FormPresensiPulang()
        konteks={
            'form':form
        }
    return render(request,'Back-end/PresensiPulang/add_presensi.html',konteks)

def hapuspresensipulang(request,id_presensi):
    presensipulang =PresensiPulang.objects.get(id=id_presensi)
    presensipulang.delete()
    messages.success(request,"Data berhasil dihapus")
    return redirect ('/presensi')