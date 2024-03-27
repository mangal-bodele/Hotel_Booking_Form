from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"

        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control'}),
            'person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows':5,'class':'form-control'}),
            'check_in': forms.DateTimeInput(attrs={'class':'form-control'}),
            'check_out': forms.DateTimeInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})

        }