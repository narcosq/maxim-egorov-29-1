from django.shortcuts import render, redirect
from posts.models import Product, Categories
from posts.forms import ProductCreateForm, CategoryCreateForm
from django.contrib.auth.decorators import login_required


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context_data = {
            'products': products,
            'user': request.user
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Categories.objects.all
        context_data = {
            'categories': categories
        }

        return render(request, 'products/categories.html', context=context_data)


def product_detail(request, pk):
    if request.method == 'GET':
        try:
            products = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, 'products/detail.html')
        context_data = {
            'product': products
        }

        return render(request, 'products/detail.html', context=context_data)


@login_required(login_url='/products/')
def product_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, file = request.POST, request.FILES
        form = ProductCreateForm(data, file)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                categories=form.cleaned_data.get('categories')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


@login_required(login_url='/categories/')
def categories_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': CategoryCreateForm
        }
        return render(request, 'products/categories.create.html', context=context_data)
    if request.method == 'POST':
        data = request.POST
        form = CategoryCreateForm(data)

        if form.is_valid():
            Categories.objects.create(
                title=form.cleaned_data.get('title'),
            )
            return redirect('/categories/')

        return render(request, 'products/categories.create.html', context={
            'form': form
        })