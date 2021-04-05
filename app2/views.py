from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>hi welcome to home page 2</h1>")
def samp2(request):
    return render(request,"sample2.html")

# Create your views here.
