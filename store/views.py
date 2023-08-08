from django.shortcuts import render
from .models import Category,Product




def index(request):
    
    return render(request, "store/index.html")





# Create your views here.
