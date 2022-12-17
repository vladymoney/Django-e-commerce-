from django import forms
from django import forms
from .models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"


