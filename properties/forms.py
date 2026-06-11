from django import forms 
from properties.models import allproperties

class PropertiesForm(forms.ModelForm):
        
    class Meta:
        model=allproperties
        fields='__all__'

class PropertiesEditForm(forms.ModelForm):
    class Meta:
        model=allproperties
        fields='__all__'
        
# class BookForm(forms.ModelForm):
#     class Meta:
#         book=Book
#         fields='__all__'
        
