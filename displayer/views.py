from django.shortcuts import render
from dashCode import gdp_test

# Create your views here.
def homepage(request):
    return render(request, "index.html")


def gdp_view(request):
    return render(request, "base.html")
