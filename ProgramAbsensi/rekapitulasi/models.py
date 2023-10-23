from django.db import models
from biodata.models import Biodata
from absensi.models import Absen
from presensi.models import Presensi
from perizinan.models import Perizinan

class Rekap(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE)
    absen_id=models.ForeignKey(Absen,on_delete=models.CASCADE)
    presensi_id=models.ForeignKey(Presensi,on_delete=models.CASCADE)
    perizinan_id=models.ForeignKey(Perizinan,on_delete=models.CASCADE)

    def total_rekap(self):
        self.absen_id=self.nama.absen_set.count()
        self.presensi_id=self.nama.presensi_set.count()
        self.perizinan_id=self.nama.perizinan_set.count()

    def save(self, *args, **kwargs):
        self.total_rekap()
        super().save(*args, **kwargs)