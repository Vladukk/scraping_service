from django.shortcuts import render

from scraping.forms import FindForm
from .models import Vacancy

def home_view(requst):

        #print(requst.GET)
    form = FindForm()
    city = requst.GET.get('city')
    language = requst.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city

        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    return  render(requst, 'scraping/home.html', {'object_list': qs, 'form': form})

# Create your views here.
