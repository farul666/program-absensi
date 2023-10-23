from django.shortcuts import render, redirect
from perizinan.forms import FormPerizinan
from perizinan.models import Perizinan
from django.contrib import messages
from biodata.models import Biodata
# from django.http import JsonResponse


def data_izin(request):
    perizinan=Perizinan.objects.all()
    biodata=Biodata.objects.all()
    konteks={
        'perizinan':perizinan,
        'biodata':biodata,
    }
    # return JsonResponse(konteks, status=200, safe=False)
    return render (request,'Back-end/Perizinan/data_perizinan.html',konteks)

# Method untuk menambahkan data pada tabel perizinan
def add_izin(request):
    form = FormPerizinan(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormPerizinan()
        konteks = {
            'form' : form,
        }
        return render(request,'Back-end/Perizinan/add_perizinan.html',konteks)
    else:
        form=FormPerizinan()
        konteks = {
            'form' : form,
        }
    return render(request,'Back-end/Perizinan/add_perizinan.html',konteks)

#Method untuk edit data pada tabel perizinan
def update_izin(request,id_perizinan) :
    perizinan=Perizinan.objects.get(id=id_perizinan)
    if request.POST:
        form = FormPerizinan(request.POST,instance=perizinan)
        if form.is_valid():
            form.save()
            messages.success (request , "Data Berhasil Diubah")
            return redirect('update_izin',id_perizinan=id_perizinan)
    else:
        form=FormPerizinan(instance=perizinan)
        konteks = {
            'form' : form,
            'perizinan':perizinan
        }
    return render(request,'Back-end/Perizinan/ubah_perizinan.html',konteks) 


#Method untuk menghapus data pada tabel perizinan
def hapus_izin(request, id_perizinan ):
    perizinan=Perizinan.objects.get(id=id_perizinan )
    perizinan.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('/perizinan')