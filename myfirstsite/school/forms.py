from django.forms import ModelForm
from .models import Product

class ProductForm (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('prod_name',)
