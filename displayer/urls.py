from django.conf.urls.static import static
from django.urls import path

from where import settings
from . import views

urlpatterns = [
                  path('', views.homepage, name = 'homepage'),
                  path("gdp", views.gdp_view, name = "sdsd"),
              ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
