""" from django.urls import path
from .views import products, home, contact, members, order, purchase, github

urlpatterns = [
    path("products", products, name="products"),
    path("", home, name="home"),
    path("contact", contact, name="contact"),
    path("members", members, name="members"),
    path("order", order, name="order"),
    path("purchase", purchase, name="purchase"),
    path("github", github, name="github"),
] """