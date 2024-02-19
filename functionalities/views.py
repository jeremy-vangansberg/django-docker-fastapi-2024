from django.shortcuts import render
from .models import Functionalities
from django.views.generic import ListView, DetailView

class FunctionalitiesListView(ListView):
    model = Functionalities
    template_name = "functionalities/funct_list.html"


class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/funct_detail.html"