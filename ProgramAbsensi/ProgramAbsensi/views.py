from django.shortcuts import render, redirect
from absensi.models import Absen
from biodata.models import Biodata
from presensi.models import Presensi
from perizinan.models import Perizinan
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    jml_absen=Absen.objects.count()
    jml_bio=Biodata.objects.count()
    jml_pre=Presensi.objects.count()
    jml_izin=Perizinan.objects.count()

    konteks={
        'jml_absen':jml_absen,
        'jml_bio':jml_bio,
        'jml_pre':jml_pre,
        'jml_izin':jml_izin
    }
    return render(request,'index.html',konteks)

# Method register

def daftar(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username sudah terpakai")
            return redirect('/register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email sudah didaftarkan")
            return redirect('/register')
        
        if len(username)>20:
            messages.error(request, "Username harus di bawah 20 karakter!!")
            return redirect('/register')
        
        if password1 != password2:
            messages.error(request,"Password tidak sama!!")
            return redirect('/register')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Akunmu berhasil di daftarkan!!")

        return redirect('/register')
    
    return render(request,"register.html")

# Method Login
def masuk(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname = user.first_name

            konteks={
                'fname':fname,
            }

            return render(request, "index.html",konteks)
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/')
        
    return render(request,"login.html")

#Method Logout
def keluar(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/login')