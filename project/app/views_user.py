from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    Listproduct= {'Product' : Product.objects.all()}
    return render(request, 'project/index.html', Listproduct)