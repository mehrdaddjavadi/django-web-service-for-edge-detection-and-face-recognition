from django import forms
from .models import FaceRecognition


class FaceRecognitionForm(forms.ModelForm):
    
    
    class Meta:
        fields=['image']
        # fields=['image','T_parameters','V_parameters','C_parameters']
        model=FaceRecognition
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})