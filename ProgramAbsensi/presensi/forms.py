from django.forms import ModelForm
from presensi.models import *
from django import forms


class FormPresensi(ModelForm):
    class Meta :
        model=Presensi
        fields='__all__'

        widgets = {
            'nama':forms.Select({'class':'form-control'}),
            'status':forms.TextInput({'class':'form-control'}),
        }

class FormPresensiPulang(ModelForm):
    class Meta :
        model=PresensiPulang
        fields='__all__'

        widgets = {
            'nama':forms.Select({'class':'form-control'}),
            'status':forms.TextInput({'class':'form-control'}),
        }