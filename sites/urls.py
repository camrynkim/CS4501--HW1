from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("home/search", views.search, name="search"),
    path("home/search/submit", views.submit, name="submit"),
    path("home/search/information", views.information, name="information"),
    path("checkout", views.checkout, name="checkout"),
    path("checkout/submit", views.submit2, name="submit2"),
    path("checkout/finish", views.finish, name="finish"),
]
