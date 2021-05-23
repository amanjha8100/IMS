from django import forms
from .models import Product

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

    def __init__(self, *args, **kwargs):
        super(AddProduct,self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'type':'text','id':'name','name':'name','class':'form-control','placeholder':'Product Name'})
        # self.fields['category'].widget = forms.Select(attrs={'class':'form-select'})
        self.fields['quantity'].widget = forms.NumberInput(attrs={'type':'number','class':'form-control','id':'quantity','name':'quantity','placeholder':'Quantity'})