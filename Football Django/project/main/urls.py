from django.urls import path
from . import views

urlpatterns = [
path("team/<int:id>", views.teamIndex, name="teamIndex"),
path("teams", views.teamsList, name="teamsList"),
path("championship/<int:id>", views.championshipIndex, name="championshipIndex"),
path("championships", views.championshipsList, name="championshipsList"),
path("visitor", views.visitorPlace, name="visitorPlace"),
path("", views.home, name="home")
]