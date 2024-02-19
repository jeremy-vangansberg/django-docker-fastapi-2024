from django.shortcuts import render
from .utils import mutliplicate_by_5

# Create your views here.
def home_page(request):

    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request):
    return render(request, 'main/contact_page.html')