from django.db import models
from biodata.models import Biodata
from datetime import datetime


class Presensi(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=10)
    tgl=models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.nama.nip
    


# Create your models here.
