from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Welcome to my home page</h1>')
    #return render(request, 'home.html')
    return render(request,'home.html',{'Name': 'Luis Miguel'})
