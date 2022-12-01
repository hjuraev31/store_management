from django import forms

from .models import Truck, Product, InfoByDate

class TruckForm(forms.ModelForm):

    class Meta:
        model = Truck
        fields = '__all__'
        labels = {
            "select" : "Truck xodimi",
            "input": "Truck nomi", 
            
        }

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ProductForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ProductForm, self).save(commit=False)
        inst.truck = self._user
        if commit:
            inst.save()
        return inst

class ProductToEditForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

            
class InfoByDateForm(forms.ModelForm):
    
    class Meta:
        model = InfoByDate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(InfoByDateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(InfoByDateForm, self).save(commit=False)
        inst.truck = self._user
        if commit:
            inst.save()
        return inst
