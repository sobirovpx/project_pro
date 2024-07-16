from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from app.forms import ProductForm, ProductModelForm
from app.models import Product
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


class ProductListView(View):

    def get(self, request):
        page = request.GET.get('page', '')
        products = Product.objects.all().order_by('-id')
        paginator = Paginator(products, 2)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {
            'page_obj': page_obj
        }
        return render(request, 'app/index.html', context)


class AddProductView(View):
    def get(self, request):
        form = ProductModelForm()
        return render(request, 'app/add-product.html', {'form': form})

    def post(self, request):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


class EditProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        form = ProductModelForm(instance=product)
        return render(request, 'app/update-product.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        form = ProductModelForm(instance=product, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk)


class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if product:
            product.delete()
            return redirect('index')


class ProductDetailTemplateView(TemplateView):
    template_name = 'app/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=kwargs['product_id'])
        context['product'] = product
        context['attributes'] = product.get_attributes()
        return context


class EditProductTemplateView(TemplateView):
    template_name = 'app/update-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=kwargs['pk'])
        context['form'] = ProductModelForm(instance=product)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        product = get_object_or_404(Product, id=kwargs['pk'])
        form = ProductModelForm(instance=product, data=request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('index')
