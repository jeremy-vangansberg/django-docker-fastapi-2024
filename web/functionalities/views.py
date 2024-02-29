from django.shortcuts import render
from .models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from main.models import User
from django.core.mail import send_mail

class FunctionalitiesListView(LoginRequiredMixin, ListView):
    model = Functionalities
    template_name = "functionalities/funct_list.html"


class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/funct_detail.html"

class UserCreationFromCustom(UserCreationForm):
    class Meta(UserCreationForm.Meta) :
        model = User


from mailjet_rest import Client
import os
api_key = '2a1dd2b3d727f9278e20e0b512f876df'
api_secret = '8f29d9e22f60e338dead18ae3df3e769'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "jeremy.vangansberg@gmail.com",
        "Name": "Jérémy"
      },
      "To": [
        {
          "Email": "jeremy.vangansberg@gmail.com",
          "Name": "Jérémy"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}


class SignupView(CreateView):
    form_class = UserCreationFromCustom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False  # Ne pas activer le compte immédiatement
        user.save()
        self.send_confirmation_email(user)
        return response

    def send_confirmation_email(self, user):
        mailjet.send.create(data=data)

    def get_success_url(self):
        # Rediriger vers une page informant l'utilisateur de vérifier son email
        return reverse_lazy('home')