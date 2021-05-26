from django import forms
from django.forms import fields
from .models import Product,Order

class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']

    def __init__(self, *args, **kwargs):
        super(AddProduct,self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'type':'text','id':'name','name':'name','class':'form-control','placeholder':'Product Name'})
        # self.fields['category'].widget = forms.Select(attrs={'class':'form-select'})
        self.fields['quantity'].widget = forms.NumberInput(attrs={'type':'number','class':'form-control','id':'quantity','name':'quantity','placeholder':'Quantity'})

class MakeOrder(forms.ModelForm):
    class Meta:
        model= Order
        fields = ['product','oquantity']

    def __init__(self, *args, **kwargs):
        super(MakeOrder,self).__init__(*args,**kwargs)
        # self.fields['product'].widget = forms.Select(attrs={'class':'form-control'})
        self.fields['oquantity'].widget = forms.NumberInput(attrs={'type':'number','class':'form-control','id':'quantity','name':'oquantity','placeholder':'Quantity'})