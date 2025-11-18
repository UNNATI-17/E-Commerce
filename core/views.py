from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from core.models import ProductReview, Product, Category,Vendor, CartOrder, CartOrderItems, ProductImages, wishlists, Address

# Create your views here.

def index(request):
    product = Product.objects.filter(product_status = "published", featured = True)
    context = {
        "products": product
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    product = Product.objects.all().order_by("-id")
    context = {
        "products": product
    }
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all().annotate(product_count = Count("products"))
    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.annotate(
        product_count=Count('products')  
    ).get(cid=cid)
    products = Product.objects.filter(
        product_status="published",
        category=category
    )
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "core/category-product-list.html", context)
