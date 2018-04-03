from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

#Returns rendered "home_page.html" when base url calls home_page function from urls.py
def home_page(request):
    return render(request, "index.html")

def contact_us(request):
    return render(request, "contact_us.html")

