from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>hi welcome to home page 1</h1>")
def samp1(request):
    return render(request,"sample1.html")
# Create your views here.
