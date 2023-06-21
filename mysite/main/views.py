from django.shortcuts import render
from django.http import HttpResponse
from .models import Model

def index(request):
    return render(request, 'main/index.html')     #первое, что мы пишем в функцию render() будет наш
    # request, вторым же будет название нашего HTML шаблона который мы используем
# Create your views here.
def index2(request):
    a = Model.objects.create(name="New name", x='s'*100)
    return HttpResponse("<h1>Hello</h1> {} -- {} <br> {}".format(a.name, a.number, a.x))
def about(request):
    return render(request, 'main/about.html')
    #return HttpResponse("<h4>Проверка работы</h4>")

def index1(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def myprojects(request):
    return render(request, 'main/myprojects.html')

def myproject1(request):
    return render(request, 'main/myproject1.html')

