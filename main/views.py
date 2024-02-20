from django.shortcuts import render
from .utils import mutliplicate_by_5
from django.contrib.auth.decorators import login_required
from .forms import CryptoApiForm

@login_required
def api_page(request):
        # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CryptoApiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    else:
        form = CryptoApiForm()

    return render(request, "main/api_page.html", context={'form':form})



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

