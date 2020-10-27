from django.shortcuts import render

from .models import Vacancy

def home_view(requst):
    qs = Vacancy.objects.all()
    return  render(requst, 'scraping/home.html', {'object_list': qs})

# Create your views here.
