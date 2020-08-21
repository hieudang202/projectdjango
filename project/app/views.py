from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def index(request):
    Listproduct= {'Product' : Product.objects.all()}
    return render(request, 'project/index.html', Listproduct)