from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm, CategoryForm
from .models import Product
from django.shortcuts import redirect




# Create your views here.

def form_view(request):
   
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    content = {'django_form':form}
    return render(request, template_name="products/addproduct_form.html", context=content)

def welcome_page(request):

    text = 'This is a small project to implement CRUD operations in Django'
    product_list = Product.objects.all()
    content = {
               'text' : text,
               'products' : product_list
              }

    return render(request, template_name='welcome_page.html' , context = content)


def view_products(request):

    product_list = Product.objects.all()
    content = {'products' : product_list}

    return render(request, template_name='products/view_products.html', context = content)

def view_product(request, id):

    product = Product.objects.get(pk=id)

    content = { 'product' : product }

    return render(request, template_name='products/view_product.html', context = content)



def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()

    return render(request, template_name='products/deleted.html')

def edit_product(request, id):

    form = ProductForm()

    product = Product.objects.get(pk=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        #this will create new model
        #form = ProductForm(request.POST)

        #this will update existing model
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()



    return render (request, template_name='products/edit_products.html', context = {'form' : form})

    


def create_category(request):

    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    

    return render(request, template_name='add_cat.html', context={'form':form} )
