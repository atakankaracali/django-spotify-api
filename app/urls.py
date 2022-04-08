from django.urls import path
from . import views
from .views import musicList


urlpatterns = [
    path("", views.index, name="index"),
    path("tracks/", views.tracks, name="tracks"),
    path("tracks/detail/", musicList.as_view(), name="rest"),
    # path("tracks/<str:trackName>/", views.detail, name="detail"),
]
