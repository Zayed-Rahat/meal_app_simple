from django.urls import path
from . import views
urlpatterns = [
    path('', views.meals_view, name = "meals_page")
]