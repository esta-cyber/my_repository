from django import forms
from .models import Studentlar


class StudentForm(forms.ModelForm):
    class Meta:
        model = Studentlar
        fields = ['name', 'surname', 'email', 'age']
        # labels = {
        #     'name': "Ism",
        #     'surname': "Familiya",
        #     'email': "Email",
        #     'age': "Yosh",
        # }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Ismingiz", 'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'placeholder': "Familiyangiz", 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': "email@misol.uz", 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
        }
