from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class AboutPageView(TemplateView):
  template_name = 'about.html'

class SignUpView(CreateView): 
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'