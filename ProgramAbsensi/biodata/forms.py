from django.forms import ModelForm
from biodata.models import Biodata
from django import forms


class FormBiodata(ModelForm):
    class Meta :
        model=Biodata
        fields='__all__'

        widgets = {
            'nip':forms.TextInput({'class':'form-control'}),
            'nama':forms.TextInput({'class':'form-control'}),
            'jk':forms.Select({'class':'form-control'}),
            'agama':forms.Select({'class':'form-control'}),
            'alamat':forms.Textarea({'class':'form-control'}),
            'mapel':forms.TextInput({'class':'form-control'}),
        }