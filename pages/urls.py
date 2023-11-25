from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("bio/", views.bio, name="bio"),
    path("skills/", views.skills, name="skills"),
]