from django.forms import ModelForm
from perizinan.models import Perizinan
from django import forms


class FormPerizinan(ModelForm):
    class Meta :
        model= Perizinan
        fields='__all__'

        widgets = {
            'nama':forms.Select({'class':'form-control'}),
            'keterangan':forms.TextInput({'class':'form-control'}),
        }
