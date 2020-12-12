from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *


# HOME PAGE
def home(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html', {'products': products})


# PRODUCT DETAIL VIEW
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    review_list = ProductReview.objects.filter(product=pk)
    # PAGINATOR OF REVIEW LIST
    paginator = Paginator(review_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    return render(request, 'Store/detail.html', {'product': product, 'reviews': reviews})


# PRODUCT LIST VIEW
def product_list(request, pk):
    sub_category = SubCategory.objects.get(pk=pk)
    products = Product.objects.filter(sub_category=sub_category)
    return render(request, 'Store/product_list.html', {'sub_category': sub_category, 'products': products})


# PRODUCT LIST VIEW
def add_review(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        data = ProductReview()
        data.product = product
        data.user = request.user
        data.name = request.POST.get('name')
        data.subject = request.POST.get('subject')
        data.rating = request.POST.get('rating')
        data.comment = request.POST.get('comment')
        data.save()
        messages.success(request, "Thanks for your review.")
        return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))
    return HttpResponseRedirect(reverse('store:product_detail', kwargs={'pk': product.pk}))