from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", main, name="url"),
    path("price/<str:type_service_glob>/", price, name="price"),
    path("shop/<str:brand>/<str:category>", shop, name="all_prod"),
    path("<str:type>/product/about_product/<int:product>", product, name="about_product"),
    path("blog/", blog, name="blog"),
    path("promoution/", promoution, name="promoution"),
    path("contacts/", contacts, name="contacts"),
]