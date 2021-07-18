from django import forms

class UploadFileForm(forms.Form):
    v3file = forms.FileField(max_length=50, label="Filename")