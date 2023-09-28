import re

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "sites/index.html")


def home(request):
    return render(request, "sites/home.html")


def search(request):
    return render(request, "sites/search.html")


def submit(request):
    if request.POST["Search"] in ["HERSHEY’S Milk Chocolate Candy Bar", "SOUR PATCH KIDS Watermelon", "REESE’S Milk "
                                                                                                      "Chocolate "
                                                                                                      "Peanut Butter "
                                                                                                      "Cups",
                                  "STARBURST Original Fruit Chews", "KIT KAT Milk Chocolate Wafer Candy Bars"]:
        return render(request, "sites/checkout.html")
    else:
        return render(request, "sites/error.html")


def information(request):
    return render(request, "sites/information.html")


def checkout(request):
    return render(request, "sites/checkout.html")


def submit2(request):
    creditcard = request.POST["creditcard"]
    firstname = request.POST["firstname"]
    number = request.POST["number"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    address = request.POST["address"]

    # isdigit method: https://www.geeksforgeeks.org/python-check-whether-string-contains-only-numbers-or-not/#:~:text=Check%20if%20String%20Contains%20Only%20Numbers%20using%20isdigit()%20method,%2C%20It%20returns%20“False”.
    # isalpha method: https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,!%23%25%26%3F%20etc.
    # regular expression to check email is valid: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not str(creditcard).isdigit() or len(str(creditcard)) != 16 or str(firstname).isalpha() is False or str(
            lastname).isalpha() is False or str(number).isdigit() is False or len(str(number)) != 10 or re.fullmatch(
        regex_email, email) is None or len(str(address)) < 1:
        return render(request, "sites/checkout_error.html")
    else:
        return render(request, "sites/confirmation.html")


def finish(request):
    return render(request, "sites/finish.html")