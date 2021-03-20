from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
# Create your views here.

def base(request):
    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    return render(request, 'main/base.html', {'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar})

def index(request):
    sub_category_navbar = sub_category.objects.all
    catalog_mainpage = catalog.objects.order_by('-id')[:4]
    furnite_mainpage = Furnite.objects.order_by('-id')[:4]
    catigories_navbar = category.objects.all
    furnite_navbar = Furnite_category.objects.all
    return render(request, 'main/index.html', {'catalog_mainpage': catalog_mainpage, 'catigories_navbar':catigories_navbar, 'sub_category_navbar':sub_category_navbar, 'furnite_mainpage': furnite_mainpage})


def all_items(request):
    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    all_items_page = catalog.objects.filter(category_id = '1')
    return render(request, 'main/all_items.html', {'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar, 'all_items_page': all_items_page})

def sizes(request):
    sub_category_navbar = sub_category.objects.all
    catigories_navbar = category.objects.all
    return render(request, 'main/sizes.html', {'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar})

def show_post(request, post_slug):

    post = get_object_or_404(catalog, slug=post_slug)
    catalog_post = catalog.objects.all
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    context = {
        'post' : post
    }

    return render(request, 'main/post.html', {'post': post, 'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar,},)

def show_furnite(request, furnite_slug):

    furnite = get_object_or_404(Furnite, slug=furnite_slug)
    furnite_post = Furnite.objects.all
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    return render(request, 'main/furnite.html', {'furnite': furnite, 'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar})

def show_category(request, category_slug):

    incategory = get_object_or_404(category, slug=category_slug)
    category_catalog = catalog.objects.order_by('-id')
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all

    context = {
        'incategory' : incategory
    }

    return render(request, 'main/category.html', {'incategory': incategory, 'catigories_navbar': catigories_navbar, 'category_catalog': category_catalog, 'sub_category_navbar':sub_category_navbar})

def show_sub_category(request, sub_category_slug):

    subcategory = get_object_or_404(sub_category, slug=sub_category_slug)
    catigories_navbar = category.objects.all
    sub_category_navbar = sub_category.objects.all
    subcategory_catalog = catalog.objects.order_by('-id')

    return render(request, 'main/subcategory.html', {'subcategory': subcategory, 'catigories_navbar': catigories_navbar, 'sub_category_navbar':sub_category_navbar, 'subcategory_catalog':subcategory_catalog})