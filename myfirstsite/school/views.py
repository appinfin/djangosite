from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.
# Функции представления страниц
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request):
    return render(request, 'school/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'school/about.html', {'menu': menu, 'title': 'О нас'})

# def index(request): #HttpRequest
#     return HttpResponse("SITE SCHOOL \
#                         <br><a href='http://127.0.0.1:8000/prod/4747'>ПРОДУКТЫ</a> \
#                         <br><a href='http://127.0.0.1:8000/archive/2023'>АРХИВЫ</a>")

def archive(request, year):
    if int(year) > 2024:
        # raise Http404()
        # return redirect ('/') #302 URL перемещён временно
        return redirect ('home', permanent = True) #301 URL перемещён постоянно
    return HttpResponse(f"АРХИВ - {year}")

def products(request, prodid): #HttpRequest
    if(request.GET):
        print(request.GET)
    
    return HttpResponse(f"products page {prodid}")

def pageNotFound(request, exception): #HttpRequest
    return HttpResponseNotFound(f"<H1>PAGE NOT FOUND</H1>")