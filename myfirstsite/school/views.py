from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("SITE SCHOOL \
                        <br><a href='http://127.0.0.1:8000/prod'>ПРОДУКТЫ</a>")

def products(request, prodid): #HttpRequest
    return HttpResponse(f"products page {prodid}")