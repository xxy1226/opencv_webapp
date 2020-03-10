from django import forms
class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    #file = forms.Filefield()
    image = forms.ImageField()
    
from .models import ImageUploadModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description','document')