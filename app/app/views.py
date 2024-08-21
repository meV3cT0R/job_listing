from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect
import sys
sys.path.append("..")
from scraper import scrape

def home(request):
    form = SearchForm()
    return render(request,"home2.html",{"form" : form})
    

def output(request):
    form = SearchForm(request.GET)
    if not form.is_valid():
        return HttpResponseRedirect("home")
    data = scrape(form.cleaned_data["search"])
    return render(request,"output.html",{"data" : data})