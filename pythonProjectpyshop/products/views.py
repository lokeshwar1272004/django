from django.shortcuts import render
from django.http import HttpResponse
from .models import data



def index(request):
    products = data.objects.all()
    return render(request, 'index.html', {'products':products})
def new(request):
    return HttpResponse('WELCOME WHAT YOU WANT')