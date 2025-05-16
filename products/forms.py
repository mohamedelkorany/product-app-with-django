from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = '__all__'

class RegisterForm (forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()