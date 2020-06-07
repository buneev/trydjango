from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import ProductForm, RawProductForm
from .models import Product

# no use
class ProductCreate(View):
    def get(self, request):
        form = ProductForm
        context = {
            'form': form
        }
        return render(request, "products/product_create.html", context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # метод is_valid() вызывает все clean_ методы формы,
            # очищенные данные попадают в словарь cleaned_data,
            # иначе validation_error() 
            new_post = form.save()
            # return redirect(new_post)

def product_create_view(request):
    init_data = {
        'title': "My this awesome title"
    }
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            # return redirect()
    else:
        form = ProductForm(initial=init_data) # инициализируем поля
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail_view(request, id):
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


# TODO: Необходим рефакторинг
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)
