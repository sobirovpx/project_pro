from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ProductForm, ProductModelForm
from app.models import Product


def index(request):
    products = Product.objects.all().order_by('-id')[:4]
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()

    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-detail.html', context)


def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)


class LoginForm:
    pass


def login(request):


    return render(request ,'app/login.html',content_type='text/html')

def register(request):


    return render(request ,'app/register.html',content_type='text/html')

def logout(request):


    return render(request ,'app/logout.html',content_type='text/html')