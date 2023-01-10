from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views

class HomeView(views.TemplateView):
    template_name = "core/home.html"

class AboutView(views.TemplateView):
    template_name = "core/about.html"

class ContactView(views.TemplateView):
    template_name = "core/contact.html"
    
