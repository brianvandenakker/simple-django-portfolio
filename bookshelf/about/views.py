from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from about.models import About
from about.forms import AboutForm
# Create your views here.

class AboutListView(ListView):
    model = About


class CreateAboutView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AboutForm

    model = About
