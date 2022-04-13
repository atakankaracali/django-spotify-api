from http import HTTPStatus
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import music_app
from .serializers import musicSerializer


def index(request):
    if request.method == "POST":
        artist_url = request.POST.get("uri")
        spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id="YOUR CLIENT ID",
                client_secret="YOUR CLIENT SECRET",
            )
        )
        results = spotify.artist_top_tracks(artist_url)
        final_result = results["tracks"][:10]
        return render(request, "index.html", {"results": final_result})
    else:
        return render(request, "index.html", status=HTTPStatus.METHOD_NOT_ALLOWED)


def tracks(request):
    if request.method == "POST":
        artist_url = "https://open.spotify.com/artist/5ixQSDvAMa5O758xG8MWXT?si=03---2GrTY60Tf4ZtW_WBA"
        spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id="YOUR CLIENT ID",
                client_secret="YOUR CLIENT SECRET",
            )
        )
        results = spotify.artist_top_tracks(artist_url)
        for track in results["tracks"][:10]:
            print("track    : " + track["name"])
            print("audio    : " + track["preview_url"])
            print("cover art: " + track["album"]["images"][0]["url"])
            print()
        return render(request, "tracks.html", track)
    else:
        return render(request, "tracks.html")


class musicList(APIView):
    def get(self, request):
        musics = music_app.objects.all()
        serializer = musicSerializer(musics, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# def detail(request):
#     if request.method == "POST":
#         artist_url = "https://open.spotify.com/artist/5ixQSDvAMa5O758xG8MWXT?si=03---2GrTY60Tf4ZtW_WBA"
#         spotify = spotipy.Spotify(
#             client_credentials_manager=SpotifyClientCredentials(
#                 client_id="YOUR CLIENT ID",
#                 client_secret="YOUR CLIENT SECRET",
#             )
#         )
#         results = spotify.artist_top_tracks(artist_url)
#     for track in results["tracks"][:10]:
#         print("track    : " + track["name"])
#         print("audio    : " + track["preview_url"])
#         print("cover art: " + track["album"]["images"][0]["url"])
#         print()
#         return render(request, "detail.html", track)
#     else:
#         return render(request, "detail.html")
