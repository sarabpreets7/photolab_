from django import forms
from .models import Userpics

class userpicsform(forms.ModelForm):
    class Meta():
        model = Userpics
        fields = ['user','photo_main', 'photo_1', 'photo_2', 'photo_3','photo_4','photo_5','photo_6']


