from django             import forms
from ..models.declarant import Declarant  

class DeclarantForm(forms.ModelForm): 
    class Meta: 
        model = Declarant
        fields = '__all__'
        #fields = ['first_name', 'last_name', 'age', 'gender']
        widgets = {
            'first_name'  : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': False}),
            'last_name'   : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': False}),
            'age'         : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age', 'required': False}),
            'gender'      : forms.Select(choices=[('M', 'Homme'), ('F', 'Femme')], attrs={'class': 'form-control'}),
        }
