from django.shortcuts import render, redirect
from biodata.forms import FormBiodata
from biodata.models import Biodata
from django.contrib import messages


# Method untuk menampilkan data pada app Biodata yang terdapat pada database
def data(request):
    biodata=Biodata.objects.all()

    konteks={
        'biodata':biodata,
    }
    return render(request,'Back-end/Biodata/data_bd.html',konteks)

# Method untuk menambahkan data pada tabel biodata
def tambahdt(request):
    form = FormBiodata(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data berhasil ditambahkan")
        form = FormBiodata()
        konteks = {
            'form' : form,
        }
        return render(request,'Back-end/Biodata/add_bd.html',konteks)
    else:
        form=FormBiodata()
        konteks = {
            'form' : form,
        }
    return render(request,'Back-end/Biodata/add_bd.html',konteks)

#Method untuk edit data pada tabel biodata
def update_dt(request,id_biodata) :
    biodatas=Biodata.objects.get(id=id_biodata)
    if request.POST:
        form = FormBiodata(request.POST,instance=biodatas)
        if form.is_valid():
            form.save()
            messages.success (request , "Data Berhasil Diubah")
            return redirect('update_dt',id_biodata=id_biodata)
    else:
        form=FormBiodata(instance=biodatas)
        konteks = {
            'form' : form,
            'biodatas':biodatas
        }
    return render(request,'Back-end/Biodata/ubah_bd.html',konteks) 

#Method untuk menghapus data pada tabel biodata
def hapusdt(request, id_biodata ):
    biodatas=Biodata.objects.get(id=id_biodata )
    biodatas.delete()
    messages.success(request ,"Data telah di hapus ")
    return redirect ('/biodata')