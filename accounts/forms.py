
from django.forms import ModelForm ,TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget


class CreatUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name',
        'email','password1','password2'
        ]

class ProfiletUser(ModelForm):
    class Meta:
        model = profile
        fields = ['phone','bio_p','photo','list_ch'
        ]
class RequetteA(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Requette_a
        fields = '__all__'
       
class RequetteF(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Requette_u
        fields = '__all__'
        exclude = ('userr','lettre')

class NewsF(ModelForm):
    
    class Meta:
        model = News
        fields = '__all__'
        

'''
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
        '''