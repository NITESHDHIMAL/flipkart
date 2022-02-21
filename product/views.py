 
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Product
from . forms import *
from django.contrib import messages


def index(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request,'product/index.html',context)


# def product_post(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect ('/product/addproduct')

#     context ={
#         'form':ProductForm
#     }
#     return render(request,'product/addproduct.html',context)


def product_post(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product Added')
       
            return redirect('/addproduct')

        else:

            messages.add_message(request,messages.ERROR,"Please verify again")
              
            return render(request, 'product/addproduct.html', {
                'form': form
            })

    context = {
        'form': ProductForm
    }
    return render(request, 'product/addproduct.html', context)





def category_post(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category Added')
            return redirect ('/product/addcategory')



        else:
            messages.add_message(request,messages.ERROR,"Pelese verify again")
              
            return render(request, 'product/addcategory.html', {
                'form': form
            })

    context ={
        'form':CategoryForm
    }
    return render(request,'product/addcategory.html',context)

 






