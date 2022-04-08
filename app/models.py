from django.db import models


class music_app(models.Model):
    trackName = models.CharField(max_length=20)
    artistName = models.CharField(max_length=70)
    exp_id = models.IntegerField()

    def __str__(self) -> str:
        return self.trackName
