from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import generics
# Create your views here.

class MapsView(TemplateView):
    template_name = "maps/maps.html"


