from django.shortcuts import render
from .utils import mutliplicate_by_5
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request, 'main/home_page.html')

def about_page(request):
    return render(request, 'main/about_page.html')

def contact_page(request, test):
    context = {'test': test}
    return render(request, 'main/contact_page.html', context=context)

@login_required
def special_page(request):
    return render(request, "main/special_page.html")

@login_required
def api_page(request):
    return render(request, "main/api_page.html")