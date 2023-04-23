from django.urls import path
from teams_leagues_viewer import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ping", views.ping, name="ping")
]
