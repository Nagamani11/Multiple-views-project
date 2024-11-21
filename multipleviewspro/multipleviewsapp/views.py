from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    x="<h1>Welcome to Home page</h1>"
    return HttpResponse(x)
def contact(request):
    x="<h1>welcome to contacts page</h1>"
    return HttpResponse(x)
def services(request):
    x="<h1>Welcome to services page</h1>"
    return HttpResponse(x)
def feedback(request):
    x="<h1>Welcome to feedback page</h1>"
    return HttpResponse(x)
