from django import forms
from .models import *



class DocumentForm(forms.ModelForm):
    class Meta:
        model = fileupload
        fields = ('field_name', )
