from django.shortcuts import render
from presensi.models import *
from absensi.models import *
from perizinan.models import *
from presensi.forms import *
from absensi.forms import *
from perizinan.forms import *
from django.contrib import messages
# Create your views here.



def homeuser(request):
    presensi=Presensi.objects.all()
    biodata=Biodata.objects.all()
    perizinan=Perizinan.objects.all()
    absen=Absen.objects.all()

    konteks={
        'presensi':presensi,
        'biodata':biodata,
        'perizinan':perizinan,
        'absen':absen,
    }
    return render(request,'Front-end/users/home_user.html',konteks)

def presensiuser(request):
    form=FormPresensi(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPresensi()
        konteks ={
            'form': form
        }
        return render(request,'Front-end/users/presensi_user.html',konteks)
    else:
        form=FormPresensi()
        konteks={
            'form':form
        }
    return render(request,'Front-end/users/presensi_user.html',konteks)

def presensipulanguser(request):
    form=FormPresensiPulang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPresensi()
        konteks ={
            'form': form
        }
        return render(request,'Front-end/users/presensipulang_user.html',konteks)
    else:
        form=FormPresensiPulang()
        konteks={
            'form':form
        }
    return render(request,'Front-end/users/presensipulang_user.html',konteks)

def absensiiuser(request):
    form=FormAbsen(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormAbsen()
        konteks ={
            'form': form
        }
        return render(request,'Front-end/users/absensi_user.html',konteks)
    else:
        form=FormAbsen()
        konteks={
            'form':form
        }
    return render(request,'Front-end/users/absensi_user.html',konteks)

def perizinanuser(request):
    form=FormPerizinan(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form=FormPerizinan()
        konteks ={
            'form': form
        }
        return render(request,'Front-end/users/perizinan_user.html',konteks)
    else:
        form=FormPerizinan()
        konteks={
            'form':form
        }
    return render(request,'Front-end/users/perizinan_user.html',konteks)