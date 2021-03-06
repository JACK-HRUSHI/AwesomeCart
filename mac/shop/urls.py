# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name='AboutUs'),
    path("cart/", views.cart, name='Cart'),
    path("contact/", views.contact, name='ContactUs'),
    path("tracker/", views.tracker, name='TrackingStatus'),
    path("search/", views.search, name='Search'),
    path("prodview/<int:myid>", views.prodView, name='ProductView'),
    path("checkout/", views.checkout, name='CheckOut')
]

urlpatterns += staticfiles_urlpatterns()
