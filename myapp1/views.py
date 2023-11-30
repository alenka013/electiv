from django.shortcuts import render

def index_page(reguest):
    return render(request, "myapp1/index.html")

# Create your views here.
