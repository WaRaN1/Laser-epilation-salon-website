from django.core.paginator import Paginator
from django.shortcuts import render
from Salon1.models import *
from Shop.models import *
from Blog.models import *
from Promoution.models import *


type_service = Type_service.objects.all()

def main(request):
    context  = Icon.objects.get(name='Logo')
    cont2 = Icon.objects.get(name='Apparat')
    plas = Icon.objects.get(name='Plas')
    preparation = Icon.objects.get(name='Preparation')
    return render(template_name="main.html", request=request, context={"context": context,
                                                                         'cont2': cont2,
                                                                         "plas": plas,
                                                                         'preparation': preparation,
                                                                         "type_service": type_service})



def price(request, type_service_glob):
    type = Type_service.objects.get(url=type_service_glob)
    context_woman = Laser_epilation.objects.filter(type=type.id) & Laser_epilation.objects.filter(gender=2)
    context_man = Laser_epilation.objects.filter(type=type.id) & Laser_epilation.objects.filter(gender=1)
    return render(template_name="price.html", request=request, context={"type": type,
                                                                        "context_woman": context_woman,
                                                                        "context_man": context_man,
                                                                        "type_service": type_service})

def shop(request, brand, category):
    if brand == "all" and category == "all":
        shop_product = Shop.objects.all() # Також є переліком товарів для пагінатора
        cat_url = "all"
        choice_cat = "Всі"
        brand_url = "all"
        choice_brand = "Всі"
    elif brand == "all" and category != "all":
        shop_product = Shop.objects.filter(category_product=Category.objects.get(name=category).id)
        cat_url = category
        choice_cat = category
        brand_url = "all"
        choice_brand = "Всі"
    elif brand != "all" and category == "all":
        shop_product = Shop.objects.filter(brand=Brand.objects.get(name=brand).id)
        cat_url = "all"
        choice_cat = "Всі"
        brand_url = brand
        choice_brand = brand
    else:
        shop_product = Shop.objects.filter(category_product=Category.objects.get(name=category).id) & Shop.objects.filter(brand=Brand.objects.get(name=brand))
        cat_url = category
        choice_cat = category
        brand_url = brand
        choice_brand = brand
    category_product = Category.objects.all()
    brand_all = Brand.objects.all()

    paginator = Paginator(shop_product, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(template_name="shop.html", request=request, context={"shop_product": shop_product,
                                                                       "category_product": category_product,
                                                                       "type_service": type_service,
                                                                       "choice_cat": choice_cat,
                                                                       "cat_url": cat_url,
                                                                       "brand_all": brand_all,
                                                                       "choice_brand": choice_brand,
                                                                       "brand_url": brand_url,
                                                                       "page_obj": page_obj
                                                                        })

def product(request, type, product):
    if type == "shop":
        product_info = Shop.objects.get(id=product)
    elif type == "blog":
        product_info = Blog.objects.get(id=product)
    return render(template_name="product_info.html", request=request, context={"product_info": product_info,
                                                                               "type_service": type_service})


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(template_name="blog.html", request=request, context={"blogs": blogs,
                                                                       "type_service": type_service,
                                                                       "page_obj": page_obj})


def promoution(request):
    promoution = Promoution.objects.all()
    context = Icon.objects.get(name='Logo')
    return render(template_name="promoution.html", request=request, context={"promoution": promoution,
                                                                             "context": context,
                                                                             "type_service": type_service})

def contacts(request):
    context = Icon.objects.get(name='Logo')
    phone_icon = Icon.objects.get(name='Phone')
    home_icon = Icon.objects.get(name='home_icon')
    mail_icon = Icon.objects.get(name='mail_icon')
    instagram_icon= Icon.objects.get(name='instagram_icon')
    viber_icon = Icon.objects.get(name='viber_icon')
    facebook_icon = Icon.objects.get(name='facebook_icon')
    return render(template_name="contacts.html", request=request, context={"context": context,
                                                                           "phone_icon": phone_icon,
                                                                           "home_icon": home_icon,
                                                                           "mail_icon": mail_icon,
                                                                           "instagram_icon": instagram_icon,
                                                                           "viber_icon": viber_icon,
                                                                           "facebook_icon": facebook_icon,
                                                                           "type_service": type_service})
