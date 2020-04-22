from django.shortcuts import render
from django.utils import timezone
from .forms import SubscriberForm
from products.models import Product, ProductImage


def landing(request):
    date = timezone.now()
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = ProductImage.objects.filter(product__is_new=True, is_main=True)
    products_images_fish = products_images.filter(product__category__id=2)
    products_images_kaef = products_images.filter(product__category__id=1)

    return render(request, 'landing/home.html', locals())


def info(request):
    return render(request, 'landing/info.html', locals())

