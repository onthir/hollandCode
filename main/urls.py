
from django.urls import path
from . import views

# declare app name to use for url routing dynamic
app_name = "main"

# define all urlpatterns here
urlpatterns = [
    path('', views.home, name="home"),
    path('questions/', views.questions, name="questions"),
    path('realistic/', views.realisticQ, name="rQ"),
    path('investigative/', views.investigativeQ, name="iQ"),
    path('artistic/', views.artisticQ, name="aQ"),
    path('social/', views.socialQ, name="sQ"),
    path('enterprising/', views.enterprisingQ, name="eQ"),
    path('conventional/', views.conventionalQ, name="cQ"),
    path('verified/', views.verified, name="verified")
]
