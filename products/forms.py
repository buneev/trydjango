from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        # Определить, какая модель будет использоваться для создания формы,
        # иначе в классе необходимо прописать все свойства
        model = Product
        # Указать, какие поля должны присутствовать в нашей форме
        fields = ['title','description','price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "Russia" in title:
            raise forms.ValidationError("This title isn't a valid")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("ru"):
            raise forms.ValidationError("This email isn't a valid")
        return email


# 1. Необходимо прописывать свойства 
# 2. Необходим метод save()
class RawProductForm(forms.Form):
    title = forms.CharField(
        label='', 
        widget=forms.TextInput(
            attrs={"placeholder": "Your title"}
        )
    )
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 10,
                'cols': 30
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

    def save(self):
        product = Product.objects.create(
            title = self.cleaned_data['title'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
        )
        return product
