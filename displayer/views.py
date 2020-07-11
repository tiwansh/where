from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "index.html")


def gdp_view(request):
    return render(request, "gdp_template.html")
