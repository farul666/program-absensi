from django.shortcuts import render
from rekapitulasi.models import Rekap
from biodata.models import Biodata

def rekap_data(request):
    rekap = Rekap.objects.filter(id=1).first()
    nama = rekap.nama if rekap else None
    
    biodata = Biodata.objects.all()
    
    konteks = {
        'nama': nama,
        'biodata': biodata,
    }

    return render(request,'rekap.html',konteks)
