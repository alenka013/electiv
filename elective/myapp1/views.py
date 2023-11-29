from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения элективы")
def loginpage(request):
    return render(request, 'myapp1/index.html')
def electivepage(request, elid):
    return HttpResponse(f"<h1>Элективы</h1><p>{elid}</p>")